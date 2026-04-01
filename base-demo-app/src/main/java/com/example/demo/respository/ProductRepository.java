package com.example.demo.repository;

import com.example.demo.model.Product;
import org.springframework.stereotype.Repository;

import java.util.*;

@Repository
public class ProductRepository {

    private final Map<UUID, Product> database = new HashMap<>();

    public List<Product> findAll() {
        return new ArrayList<>(database.values());
    }

    public Optional<Product> findById(UUID id) {
        return Optional.ofNullable(database.get(id));
    }

    public Product save(Product product) {

        if (product.getId() == null) {
            product.setId(UUID.randomUUID());
        }

        database.put(product.getId(), product);

        return product;
    }

    public void delete(UUID id) {
        database.remove(id);
    }

}