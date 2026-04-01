package com.example.demo.service;

import com.example.demo.dto.ProductDTO;
import com.example.demo.exception.ResourceNotFoundException;
import com.example.demo.model.Product;
import com.example.demo.repository.ProductRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class ProductService {

    private final ProductRepository repository;

    public ProductService(ProductRepository repository) {
        this.repository = repository;
    }

    public List<ProductDTO> listAll() {

        return repository.findAll()
                .stream()
                .map(ProductDTO::fromEntity)
                .collect(Collectors.toList());
    }

    public ProductDTO findById(UUID id) {

        Product product = repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Product not found"));

        return ProductDTO.fromEntity(product);
    }

    public ProductDTO create(ProductDTO dto) {

        Product product = dto.toEntity();

        Product saved = repository.save(product);

        return ProductDTO.fromEntity(saved);
    }

    public ProductDTO update(UUID id, ProductDTO dto) {

        Product existing = repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Product not found"));

        existing.setName(dto.getName());
        existing.setDescription(dto.getDescription());
        existing.setPrice(dto.getPrice());

        repository.save(existing);

        return ProductDTO.fromEntity(existing);
    }

    public void delete(UUID id) {

        repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Product not found"));

        repository.delete(id);
    }

}