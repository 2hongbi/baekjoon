from collections import defaultdict
import math

def subtract_time(start_time, end_time='23:59'):
    # 시작 시간과 종료 시간의 차이를 분 단위로 계산
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))
    
    total_start_minutes = start_hour * 60 + start_minute
    total_end_minutes = end_hour * 60 + end_minute
    
    return total_end_minutes - total_start_minutes


def calculate_fee(duration, fees):
    # 주차 요금 계산하기
    # fees : 기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)
    base_time, base_fee, unit_time, unit_fee = fees
    if duration <= base_time:
        return base_fee
    return base_fee + math.ceil((duration - base_time) / unit_time) * unit_fee


def solution(fees, records):
    parking_records = defaultdict(list)
    fees_dict = defaultdict(int)
    
    for record in records:
        time, car_number, status = record.split()
        if status == 'IN':
            parking_records[car_number].append(time)
        else:
            in_time = parking_records[car_number].pop()
            parked_duration = subtract_time(in_time, time)
            fees_dict[car_number] += parked_duration

    # 마지막에 출차 기록이 없는 차량들 처리
    for car_number, times in parking_records.items():
        if times:  # 출차 기록이 없는 경우
            in_time = times.pop()
            parked_duration = subtract_time(in_time)
            fees_dict[car_number] += parked_duration

    # 요금 계산
    final_fees = [(car_number, calculate_fee(duration, fees)) for car_number, duration in sorted(fees_dict.items())]

    return [fee for _, fee in final_fees]