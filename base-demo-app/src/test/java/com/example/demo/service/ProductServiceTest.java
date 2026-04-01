package com.example.demo.service;

import com.example.demo.dto.ProductDTO;
import com.example.demo.repository.ProductRepository;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.math.BigDecimal;
import java.util.List;

public class ProductServiceTest {

    private final ProductRepository repository = new ProductRepository();
    private final ProductService service = new ProductService(repository);

    @Test
    void shouldCreateProduct() {

        ProductDTO dto = new ProductDTO();

        dto.setName("Laptop");
        dto.setDescription("Gaming laptop");
        dto.setPrice(new BigDecimal("5000"));

        ProductDTO created = service.create(dto);

        Assertions.assertNotNull(created.getId());
    }

    @Test
    void shouldListProducts() {

        ProductDTO dto = new ProductDTO();

        dto.setName("Mouse");
        dto.setDescription("Wireless mouse");
        dto.setPrice(new BigDecimal("100"));

        service.create(dto);

        List<ProductDTO> products = service.listAll();

        Assertions.assertFalse(products.isEmpty());
    }

}