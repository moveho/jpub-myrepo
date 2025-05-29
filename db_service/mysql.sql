SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

CREATE DATABASE IF NOT EXISTS products CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE products;

CREATE TABLE IF NOT EXISTS products (
    prd_id INT AUTO_INCREMENT PRIMARY KEY,
    prd_name VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    category VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    origin_country VARCHAR(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    warehouse_location VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    price DECIMAL(10,2),
    stock INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 샘플 데이터
INSERT INTO products (prd_name, category, origin_country, warehouse_location, price, stock)
VALUES
('Apple', 'Fruit', 'USA', 'Seoul Warehouse', 1.20, 150),
('Banana', 'Fruit', 'Philippines', 'Busan Warehouse', 0.80, 200),
('Mango', 'Fruit', 'India', 'Incheon Hub', 1.50, 90),
('Broccoli', 'Vegetable', 'Korea', 'Daejeon Center', 1.00, 60),
('Salmon', 'Seafood', 'Norway', 'Incheon Hub', 5.40, 40);

-- 사용자 인증 테이블
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

