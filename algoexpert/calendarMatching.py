from datetime import datetime, timedelta



def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    format = '%H:%M'
    to_time = lambda x: datetime.strptime(x, format)
    time_to_add = timedelta(minutes=meetingDuration)
    ans = []
    i, j=0,0
    end1 = min(to_time(dailyBounds1[1]),to_time( dailyBounds2[1]))

    start1 = start2 = max(to_time(dailyBounds1[0]),to_time( dailyBounds2[0]))
    while i < len(calendar1) or j < len(calendar2):
        start1 = start2 = max(start1, start2)

        if i < len(calendar1) and start1  > to_time(calendar1[i][0]):
            start1 = to_time(calendar1[i][1])
            i+=1
            continue
        if j < len(calendar2) and start2  > to_time(calendar2[j][0]):
            start2 = to_time(calendar2[j][1])
            j+=1
            continue

        curr = start1
        end = min(to_time(calendar2[j][0]),to_time( calendar1[i][0]))
        if curr + time_to_add<=end and curr+time_to_add < end1:
            ans.append([curr.strftime(format), end.strftime(format)])
        start1 = start2 = min(to_time(calendar2[j][1]),to_time( calendar1[i][1]))

    curr = max(start1, start2)
    if curr + time_to_add <= end1:
        ans.append([curr.strftime(format), end1.strftime(format)])

    ans = [[x if x[0]!='0' else x[1:] for x in _] for _ in ans]
    return ans


print(calendarMatching([['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']], ['9:00', '20:00'] ,[['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']] ,['10:00', '18:30'] ,30))