---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "source-example"
source_ids: ["src-000012"]
source_edition: "Version 3.0, 2021-11-03"
curated: true
file_pages: [36]
source_locations: ["§4.5 Example"]
limitations: ["Source example retained; exact executable XML/cryptographic validity is not claimed."]
source_editions: ["Version 3.0 2021-11-03"]
---

# §4.5 Example

[src-000012](../../../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), file/printed page 36, §4.5 Example.

The source supplies a Signature example with three References, SignatureValue and KeyInfo/X509Data. The X509Certificate is abbreviated in the source. Preserve the source artwork as the authority for exact XML and sample values; text extraction introduces spacing artefacts and has not been executed as a cryptographic test vector.

[Complete original example rendered from PDF](../../../../../../../../evidence/omitted/992ec56931b412dd69e32c71.md)

## Preserved source text

This is the verbatim text extraction, including extraction spacing or replacement characters. Use the source page when exact lexical fidelity matters.

```text
36 ISO 20022 Business Application Header Message Usage Guide v3.0  
4.5  Example 
An example of a Signature within the BAH that can be verified is as follows: 
 
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig# "> 
 <ds:S ignedInfo>  
  <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml- exc-c14n#"/> 
  <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig -more#rsa- 
sha256"/> 
  <ds:Reference URI="#Unique-id-to-KeyInfo"> 
   <ds:Transforms> 
    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml -exc-c14n#"/> 
   </ds:Transforms> 
   <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256 "/> 
   <ds:DigestValue> QYYVi9JdlsOxjplrW3vIjT8cWYyzYD4ZnnNJ9SH+dvQ=  
</ds:DigestValue> 
  </ds:Reference> 
  <ds:Reference URI=""> 
   <ds:Transforms> 
    <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped- 
signature"/> 
    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml -exc-c14n#"/> 
   </ds:Transforms> 
   <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256 "/> 
   <ds:DigestValue> 
+OS/MM1NBTiOZWWpvzOWkfRjyP2/F1lg9P+zvC+Gulk=  
</ds:DigestValue> 
  </ds:Reference> 
  <ds:Reference> 
   <ds:Transforms> 
    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml -exc-c14n#"/> 
   </ds:Transforms> 
   <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256 "/> 
   <ds:DigestValue> QYYVi9JdlsOxjplrW3vIjT8cWYyzYD4ZnnNJ9SH+dvQ=  
</ds:DigestValue> 
  </ds:Reference> 
 </ds:SignedInfo> 
 <ds:SignatureValue> IKDs7kwX14CxK3AZ1ojJLr35A4eU/98tp/10KFQTtPOwR5WCKyx 
4I05ZV1IljOpEgpkt6xejXhshaEnNBD5B5PII1VN6mviJJjU/njGikNeXzi1Djei2dPEap 
nPX1f26UnQcgYTAqaSVwAnIR7L8/W2UeT8J9z8Rd1OebYV5xE8jVehbgMcAmJwv2rC/c2d 
UkUe2/eBU0APyWGCgKawxGGAPLP3AS4+Mp0ODKlVp08rUzVOF+pFF/1dBknlK/v0dWkDdj 
YvwFRvZhHXue/PYvMNtQBytMUUdB1MiQrNX0jSCE6Y2nljhTXdcrb2lgfgwCclB6xArBRV 
WfMa0kQVQ4Q== 
</ds:SignatureValue> 
 <ds:KeyInfo Id="Unique-id-to-KeyInfo"> 
  <ds: X509Data > 
   <ds:X509Certificate>MIID1DCCArygAwIB </ds:X509Certificate> 
  </ds:X509Data> 
 </ds:KeyInfo> 
</ds:Signature>
```

## Source components

