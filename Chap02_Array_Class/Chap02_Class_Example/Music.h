#pragma once
#pragma once
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Music class
class Music {
private:
    string title;
    string artist;
    string album;
    int year;
public:
    //생성자(Constructor)
    Music(string title, string artist, string album, int year) {
        this->title = title;
        this->artist = artist;
        this->album = album;
        this->year = year;
    }

    //소멸자(Destructor)
    ~Music() {}

    // Getters
    string getTitle() { return title; }
    string getArtist() { return artist; }
    string getAlbum() { return album; }
    int getYear() { return year; }
};

// MusicStreamingService class
class MusicStreamingService {
private:
    string serviceName;
    vector<Music> musicList;                     //음악 리스트는 벡터를 이용해  앞에서 있는 "music" 클래스에서 만들어진 각각의 객체들이 들어있음

public:
    MusicStreamingService(string serviceName) {
        this->serviceName = serviceName;
    }

    // Adds a music to the service
    void addMusic(string title, string artist, string album, int year) {
        Music newMusic(title, artist, album, year);    //newmusic 객체 생성
        musicList.push_back(newMusic);                 //음악 리스트에 newmusic을 넣어줌
        cout << title << " by " << artist << " added to " << serviceName << endl;
    }

    // Searches for music by title
    Music* searchByTitle(string title) {              //*은 주소값을 의미
        for (int i = 0; i < musicList.size(); i++) {
            if (musicList[i].getTitle() == title) {
                return &musicList[i];                //&가 붙어있으면 주소값
            }
        }
        return NULL;
    }

    // Searches for music by artist
    vector<Music*> searchByArtist(string artist) {
        vector<Music*> result;
        for (int i = 0; i < musicList.size(); i++) {
            if (musicList[i].getArtist() == artist) {
                result.push_back(&musicList[i]);
            }
        }
        return result;
    }

};
