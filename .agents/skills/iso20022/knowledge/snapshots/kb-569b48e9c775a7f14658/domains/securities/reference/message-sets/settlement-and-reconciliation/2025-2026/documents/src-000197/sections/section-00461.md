---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "20.4 Message Building Blocks", "20.4.18 SupplementaryData <SplmtryData>"]
file_pages: [707]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.026.001.12"]
---

# 20.4.18 SupplementaryData <SplmtryData>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 707 to 707.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 707

```text
CertificateNumber <CertNb> contains the following elements (see "SecuritiesCertificate4" on
page 1630 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] Text 1631
   Issuer <Issr> [0..1] Text 1631
   SchemeName <SchmeNm> [0..1] Text 1631
Constraints
• ISO8532AndIssuerSchemeNameRule
If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.
20.4.18 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C57 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 707 March 2026
```

