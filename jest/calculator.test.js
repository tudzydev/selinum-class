const mathOperations = require('./calculator');

describe('Math Operations', () => {
    test('sum of two numbers', () => {
        expect(mathOperations.sum(2, 3)).toBe(5);
    });

    test('difference of two numbers', () => {
        expect(mathOperations.diff(5, 3)).toBe(2);
    });

    test('product of two numbers', () => {
        expect(mathOperations.product(4, 3)).toBe(12);
    });
});