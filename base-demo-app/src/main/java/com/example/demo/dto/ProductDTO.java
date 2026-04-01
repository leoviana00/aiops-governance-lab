package com.example.demo.dto;

import com.example.demo.model.Product;

import java.math.BigDecimal;
import java.util.UUID;

public class ProductDTO {

    private UUID id;
    private String name;
    private String description;
    private BigDecimal price;

    public ProductDTO() {
    }

    public ProductDTO(UUID id, String name, String description, BigDecimal price) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.price = price;
    }

    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public void setPrice(BigDecimal price) {
        this.price = price;
    }

    // ==============================
    // Mapping
    // ==============================

    public static ProductDTO fromEntity(Product product) {

        return new ProductDTO(
                product.getId(),
                product.getName(),
                product.getDescription(),
                product.getPrice()
        );

    }

    public Product toEntity() {

        Product product = new Product();

        product.setId(this.id);
        product.setName(this.name);
        product.setDescription(this.description);
        product.setPrice(this.price);

        return product;
    }

}