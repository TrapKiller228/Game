import numpy as np



def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)



def chislo(number):

    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict:
            predict += 25
            if number > predict:
                predict += 1
            elif number < predict:
                predict -=1
            return(count)
        elif number < predict:
            predict -= 25
            if number > predict:
                predict +=1
            elif number < predict:
                predict -=1
            return(count)
    return(count)
score_game(chislo)


