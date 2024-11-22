def find_king(board):
    for i in range(len(board)):  # วนแต่ละแถว
        for j in range(len(board[i])):  # วนแต่ละคอลัมน์ในแถว
            if board[i][j] == 'K':  # ถ้าเจอ King
                return (i, j)  # คืนค่าแถว และคอลัมน์ที่เจอ King

def is_rook_checking(board, king_row, king_col):
    # ตรวจสอบการรุกในแนวตั้งและแนวนอน
    for i in range(king_row - 1, -1, -1):  # ตรวจสอบด้านบน
        if board[i][king_col] == 'R':  # เจอ Rook ที่สามารถเดินมาจับ King ได้
            return True
        elif board[i][king_col] != '.':  # เจอหมากอื่นขวาง
            break

    for i in range(king_row + 1, len(board)):  # ตรวจสอบด้านล่าง
        if board[i][king_col] == 'R':
            return True
        elif board[i][king_col] != '.':
            break

    for j in range(king_col - 1, -1, -1):  # ตรวจสอบด้านซ้าย
        if board[king_row][j] == 'R':
            return True
        elif board[king_row][j] != '.':
            break

    for j in range(king_col + 1, len(board[0])):  # ตรวจสอบด้านขวา
        if board[king_row][j] == 'R':
            return True
        elif board[king_row][j] != '.':
            break

    return False  # ถ้าไม่มี Rook ที่สามารถจับได้

def is_bishop_checking(board, king_row, king_col):
    # ตรวจสอบแนวทแยง
    for i, j in zip(range(king_row - 1, -1, -1), range(king_col - 1, -1, -1)):  # แนวทแยงซ้ายบน
        if board[i][j] == 'B':
            return True
        elif board[i][j] != '.':
            break

    for i, j in zip(range(king_row - 1, -1, -1), range(king_col + 1, len(board[0]))):  # แนวทแยงขวาบน
        if board[i][j] == 'B':
            return True
        elif board[i][j] != '.':
            break

    for i, j in zip(range(king_row + 1, len(board)), range(king_col - 1, -1, -1)):  # แนวทแยงซ้ายล่าง
        if board[i][j] == 'B':
            return True
        elif board[i][j] != '.':
            break

    for i, j in zip(range(king_row + 1, len(board)), range(king_col + 1, len(board[0]))):  # แนวทแยงขวาล่าง
        if board[i][j] == 'B':
            return True
        elif board[i][j] != '.':
            break

    return False

def is_queen_checking(board, king_row, king_col):
    return is_rook_checking(board, king_row, king_col) or is_bishop_checking(board, king_row, king_col)

def is_pawn_checking(board, king_row, king_col):
    # ตรวจสอบทแยงหน้าซ้ายและขวาของ Pawn
    if king_row > 0 and king_col > 0 and board[king_row - 1][king_col - 1] == 'P':  # ทแยงซ้ายบน
        return True
    if king_row > 0 and king_col < len(board[0]) - 1 and board[king_row - 1][king_col + 1] == 'P':  # ทแยงขวาบน
        return True
    return False

def checkmate(board):
    king_pos = find_king(board)
    if not king_pos:
        return "Fail"  # ไม่มี King บนกระดาน
    
    king_row, king_col = king_pos
    
    # ตรวจสอบว่า King ถูก "เช็ค" โดยหมากตัวใดตัวหนึ่งหรือไม่
    if is_rook_checking(board, king_row, king_col):
        return "Success"
    if is_bishop_checking(board, king_row, king_col):
        return "Success"
    if is_queen_checking(board, king_row, king_col):
        return "Success"
    if is_pawn_checking(board, king_row, king_col):
        return "Success"
    
    return "Fail"

def main():
    board = [
        "....",
        ".K..",
        "...Q",
        ".R.."
    ]
    print(checkmate(board))

if __name__ == "__main__":
    main()
