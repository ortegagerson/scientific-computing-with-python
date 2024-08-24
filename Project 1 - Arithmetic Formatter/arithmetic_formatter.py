def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_operands = []
    second_operands = []
    operator = ''
    dashes = []
    answers = []

    for problem in problems:
        if '+' in problem:
            operator = '+'
        elif '-' in problem:
            operator = '-'
        
        else:
            return "Error: Operator must be '+' or '-'."
        
        first_operand, second_operand = problem.split(operator)
        first_operand = first_operand.strip()
        second_operand = second_operand.strip()

        if not first_operand.isdigit() or not second_operand.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        max_width = max(len(first_operand), len(second_operand)) + 2
        first_operands.append(first_operand.rjust(max_width))
        second_operands.append(operator + second_operand.rjust(max_width - 1))
        dashes.append('-'*max_width)

        disp_q = '    '.join(first_operands) +'\n' + '    '.join(second_operands) + '\n' + '    '.join(dashes)

        if show_answers:
            if operator == '+':
                answer = str(int(first_operand) + int(second_operand))
            else:
                answer = str(int(first_operand) - int(second_operand))
            answers.append(answer.rjust(max_width))
            disp_q = '    '.join(first_operands) +'\n' + '    '.join(second_operands) + '\n' + '    '.join(dashes) + '\n' + '    '.join(answers)
    
    return disp_q

print(f'{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
