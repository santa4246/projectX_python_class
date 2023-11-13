def main():
    try:
        print("실행 시간 : ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
    except Exception as err :
        print("error: {0}".format(err))

if __name__ == "__main__":
    main()