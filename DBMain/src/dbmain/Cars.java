/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dbmain;


public class Cars {
    private Long id;
    private String name;
    private int price;
    private double engineVolume;

    public Cars() {
    }

    public Cars(Long id, String name, int price, double engineVolume) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.engineVolume = engineVolume;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public double getEngineVolume() {
        return engineVolume;
    }

    public void setEngineVolume(double engineVolume) {
        this.engineVolume = engineVolume;
    }
    public String toString(){
        return id+" "+name+" "+price+" "+engineVolume;
    }
    
    
    
    
}
