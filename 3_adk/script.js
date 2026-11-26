const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreElement = document.getElementById('score-value');
const gameOverScreen = document.getElementById('game-over-screen');
const winScreen = document.getElementById('win-screen');
const restartBtn = document.getElementById('restart-btn');
const restartBtnWin = document.getElementById('restart-btn-win');

// Set canvas dimensions
canvas.width = 800;
canvas.height = 600;

// Game constants
const BALL_RADIUS = 10;
const PADDLE_WIDTH = 120;
const PADDLE_HEIGHT = 15;
const BRICK_PADDING = 10;
const BRICK_OFFSET_TOP = 50;
const BRICK_OFFSET_LEFT = 30;
const BRICK_WIDTH = 75;
const BRICK_HEIGHT = 30;

// Game State
let score = 0;
let gameRunning = false;
let ball = {};
let paddle = {};
let bricks = [];
let particles = [];

// Particle Class
class Particle {
    constructor(x, y, color) {
        this.x = x;
        this.y = y;
        this.color = color;
        this.size = Math.random() * 4 + 1;
        this.speedX = (Math.random() - 0.5) * 6;
        this.speedY = (Math.random() - 0.5) * 6;
        this.life = 1.0;
        this.decay = Math.random() * 0.02 + 0.01;
    }

    update() {
        this.x += this.speedX;
        this.y += this.speedY;
        this.life -= this.decay;
    }

    draw() {
        ctx.globalAlpha = this.life;
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.closePath();
        ctx.globalAlpha = 1.0;
    }
}

// Initialize Game
function init() {
    score = 0;
    scoreElement.innerText = score;
    gameRunning = true;
    gameOverScreen.classList.add('hidden');
    winScreen.classList.add('hidden');

    ball = {
        x: canvas.width / 2,
        y: canvas.height - 50,
        dx: 4,
        dy: -4,
        speed: 4
    };

    paddle = {
        x: (canvas.width - PADDLE_WIDTH) / 2,
        y: canvas.height - 50,
        width: PADDLE_WIDTH,
        height: PADDLE_HEIGHT
    };

    // Create bricks
    const rows = 5;
    const cols = 8;
    bricks = [];
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            const brickX = c * (BRICK_WIDTH + BRICK_PADDING) + BRICK_OFFSET_LEFT;
            const brickY = r * (BRICK_HEIGHT + BRICK_PADDING) + BRICK_OFFSET_TOP;
            bricks.push({
                x: brickX,
                y: brickY,
                width: BRICK_WIDTH,
                height: BRICK_HEIGHT,
                status: 1,
                color: `hsl(${r * 40 + 200}, 80%, 50%)`
            });
        }
    }
    particles = [];
}

// Input handling
document.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;

    let paddleX = mouseX - paddle.width / 2;
    if (paddleX < 0) paddleX = 0;
    if (paddleX > canvas.width - paddle.width) paddleX = canvas.width - paddle.width;

    paddle.x = paddleX;
});

// Game Logic
function collisionDetection(b, brick) {
    return b.x + BALL_RADIUS > brick.x &&
           b.x - BALL_RADIUS < brick.x + brick.width &&
           b.y + BALL_RADIUS > brick.y &&
           b.y - BALL_RADIUS < brick.y + brick.height;
}

function createParticles(x, y, color) {
    for (let i = 0; i < 10; i++) {
        particles.push(new Particle(x, y, color));
    }
}

function drawBall() {
    ctx.beginPath();
    ctx.arc(ball.x, ball.y, BALL_RADIUS, 0, Math.PI * 2);
    // Glowing Effect
    ctx.shadowBlur = 15;
    ctx.shadowColor = '#fff';
    ctx.fillStyle = '#fff';
    ctx.fill();
    ctx.closePath();
    ctx.shadowBlur = 0;
}

function drawPaddle() {
    ctx.beginPath();
    ctx.roundRect(paddle.x, paddle.y, paddle.width, paddle.height, 10);
    ctx.fillStyle = '#00f2ff';
    ctx.shadowBlur = 15;
    ctx.shadowColor = '#00f2ff';
    ctx.fill();
    ctx.closePath();
    ctx.shadowBlur = 0;
}

function drawBricks() {
    for (let i = 0; i < bricks.length; i++) {
        const b = bricks[i];
        if (b.status === 1) {
            ctx.beginPath();
            ctx.roundRect(b.x, b.y, b.width, b.height, 4);
            ctx.fillStyle = b.color;
            ctx.shadowBlur = 10;
            ctx.shadowColor = b.color;
            ctx.fill();
            ctx.closePath();
            ctx.shadowBlur = 0;
        }
    }
}

function updateParticles() {
    for (let i = 0; i < particles.length; i++) {
        particles[i].update();
        if (particles[i].life <= 0) {
            particles.splice(i, 1);
            i--;
        } else {
            particles[i].draw();
        }
    }
}

function update() {
    if (!gameRunning) return;

    // Move ball
    ball.x += ball.dx;
    ball.y += ball.dy;

    // Wall collisions (taking radius into account)
    if (ball.x + BALL_RADIUS > canvas.width || ball.x - BALL_RADIUS < 0) {
        ball.dx = -ball.dx;
    }
    if (ball.y - BALL_RADIUS < 0) {
        ball.dy = -ball.dy;
    }

    // Bottom boundary / Paddle collision
    if (ball.y + BALL_RADIUS > canvas.height - 50) {
        if (ball.x > paddle.x && ball.x < paddle.x + paddle.width) {
            const hitPoint = (ball.x - (paddle.x + paddle.width / 2)) / (paddle.width / 2);
            ball.dy = -Math.abs(ball.dy);
            ball.dx = hitPoint * ball.speed;
            ball.y = canvas.height - 60; // Prevent sticking
        } else if (ball.y + BALL_RADIUS > canvas.height) {
            gameOver();
        }
    }

    // Brick collisions
    for (let i = 0; i < bricks.length; i++) {
        const b = bricks[i];
        if (b.status === 1) {
            if (collisionDetection(ball, b)) {
                ball.dy = -ball.dy;
                b.status = 0;
                score += 10;
                scoreElement.innerText = score;
                createParticles(b.x + b.width/2, b.y + b.height/2, b.color);

                if (score >= (bricks.length * 10)) {
                    winGame();
                }
                break;
            }
        }
    }

    // Draw everything
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBricks();
    drawPaddle();
    drawBall();
    updateParticles();

    requestAnimationFrame(update);
}

function gameOver() {
    gameRunning = false;
    gameOverScreen.classList.remove('hidden');
}

function winGame() {
    gameRunning = false;
    winScreen.classList.remove('hidden');
}

function resetGame() {
    init();
    update();
}

restartBtn.addEventListener('click', resetGame);
restartBtnWin.addEventListener('click', resetGame);

init();
update();
