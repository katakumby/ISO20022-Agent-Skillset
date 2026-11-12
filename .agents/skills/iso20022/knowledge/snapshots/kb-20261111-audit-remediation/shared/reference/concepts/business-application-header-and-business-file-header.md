---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "concept"
concept_id: "bah-versus-business-file-header"
source_ids: ["src-000011", "src-000012", "src-000013", "src-000261", "src-000349"]
message_ids: ["head.001.001.04", "head.002.001.01"]
message_families: ["head.001", "head.002"]
message_sets: ["business-application-header", "t2s-business-file-header"]
limitations: ["MUG exact-version applicability unresolved.", "Source direction inconsistency in MUG §2.13.", "MUG source conflicts remain; all supplied header figures have review evidence."]
source_editions: ["Version 3.0 2021-11-03", "Version 4 March 2024", "june-2024", "march-2024"]
---

# Business Application Header and Business File Header

The Business Application Header and Business File Header describe different exchange scopes. They have distinct full identifiers and namespaces and must not share a canonical message definition.

| Aspect | Business Application Header | Business File Header |
| --- | --- | --- |
| Supplied definition | head.001.001.04 BusinessApplicationHeaderV04 | head.002.001.01 BusinessFileHeaderV01 |
| Schema root | AppHdr | Xchg |
| Scope | A Business Message and its sending/receiving MessagingEndpoints | A file exchange, its content and structure |
| Core identifier | BusinessMessageIdentifier identifies the Business Message to its creator | PayloadIdentifier identifies the file delivered by the sender |
| Payload | BAH accompanies the ISO 20022 message; the guide permits different packaging | PayloadDescription describes the exchange; zero or more Payload elements contain exchanged documents |
| Processing context | BusinessService, MarketPractice, CreationDate, BusinessProcessingDate, copy/duplicate and related-message context | File identifier, creation timestamp, possible-duplicate flag, optional application specifics, payload type and manifest counts |
| Supplied publication evidence | MDR Version4, March2024; separate MUG Version3.0, 2021-11-03 | MDR June2024, approved 18 June2024, supplied inside T2S archive |

Evidence: [src-000011](../../../evidence/omitted/b1a725a8c57af20c03e238c2.md), file/printed pages 4–6 §2.1 and 9–16 §2.4; [src-000013](../../../raw-input/business_application_header/head.001.001.04.xsd), target namespace urn:iso:std:iso:20022:tech:xsd:head.001.001.04, /xs:schema/xs:element[@name="AppHdr"]; [src-000349](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf, file/printed pages 3–8 §§1.1,2.1–2.4; [src-000261](../../../raw-input/target2securities_t2s/head.002.001.01.xsd), target namespace urn:iso:std:iso:20022:tech:xsd:head.002.001.01, /xs:schema/xs:element[@name="Xchg"].

## Business identity and transport identity

A Business Message is the ISO 20022 message plus its BAH. A technical forwarder does not become the BAH business sender or recipient solely by transporting it. If an intermediary actually processes the Business Message, it is recipient of the first message and sender of a different second message. The standard does not prescribe AppHdr/Document order in an envelope; the MUG calls BAH-first common best practice and also permits other packaging. [src-000012](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), file/printed pages 3–5 §§1.3–1.5.

## File-header boundaries and rules

The supplied June2024 BFH publication states that head.002 is for existing implementations such as the Eurosystem and that new implementations must use the future Business File Envelope nvlp.002. This is the statement of that supplied publication; no nvlp.002 schema or current external status is established here. [src-000349](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf, file/printed pages 3–4 §§1.1,2.1.

The BFH narrative gives absent PossibleDuplicateFlag the business meaning False. The supplied XSD makes the element optional and declares no default attribute. Keep that source-defined business default distinct from XSD validation defaults. The BFH SignatureEnvelope wildcard permits XML Signature namespace content with lax processing, while MDR C1 permits only the Signature root element. The Payload wildcard accepts any namespace with lax processing. [src-000349](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf, file/printed page 5 §2.3 C1, page7 §2.4.1.1.3, page8 §2.4.2; [src-000261](../../../raw-input/target2securities_t2s/head.002.001.01.xsd), /xs:schema/xs:complexType[@name="PayloadData2"], SignatureEnvelope and LaxPayload declarations.

## Participant and flow retrieval

- [BAH scenario index](../message-sets/business-application-header/2021-11-03-v3.0/flows/index.md).
- [Sending MessagingEndpoint](../participants/bah-sending-messaging-endpoint.md).
- [Receiving MessagingEndpoint](../participants/bah-receiving-messaging-endpoint.md).
- [Business application acting as intermediary](../participants/bah-business-intermediary.md).
- [Technical intermediary that forwards a Business Message](../participants/bah-technical-forwarder.md).
- [Business File Header system user](../participants/bfh-system-user.md).
- [Business File Header system administrator](../participants/bfh-system-administrator.md).

## Known limitations

- The MUG v3.0 packaging example uses head.001.001.03, while supplied MDR and XSD define head.001.001.04. Guide-level scenarios are not silently treated as an exact V04 implementation profile.
- MUG §2.13 pp21–22 names B as sender of a newly related Business Message B, but p22 repeats a table with From A / To B. The related-message flow records that inconsistency.
- All MUG image occurrences now have dispositions and reconstruction/visual evidence. Its source conflicts remain explicit. Both MDRs have complete reviewed table/figure inventories; neither contains a substantive source diagram.
- [Direction issue issue-000003](../../../tracking/issues.md#issue-000003) and [applicability issue issue-000004](../../../tracking/issues.md#issue-000004) records unresolved corpus limitations.


## Exact references and reviewed inventories

[BAH V04 business rules](../messages/head.001.001.04/business.md) · [BFH V01 business rules](../messages/head.002.001.01/business.md) · [BAH MDR coverage](../message-sets/business-application-header/march-2024/documents/src-000011/visual-coverage.md) · [BFH MDR coverage](../message-sets/t2s-business-file-header/june-2024/documents/src-000349/visual-coverage.md).

The MDR structure tables print generic “Message root <Document>” before AppHdr (BAH p7) or Xchg (BFH p5). Actual supplied XSD global roots are AppHdr and Xchg; the preserved table labels do not establish an extra Document wrapper.
