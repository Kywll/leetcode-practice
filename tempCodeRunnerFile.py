        for friend in friends:
            dic[friend] = friend
        for num in order:
            if num in friends: 
                result.append(num)
        return num