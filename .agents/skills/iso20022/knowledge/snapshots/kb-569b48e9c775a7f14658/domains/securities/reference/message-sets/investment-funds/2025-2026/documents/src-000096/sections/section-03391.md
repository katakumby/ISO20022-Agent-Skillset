---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.10 InvestmentAccount76", "66.1.24.10.5 SecurityDetails <SctyDtls>", "66.1.24.10.5.1 Identification <Id>"]
file_pages: [4635]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.10.5.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4635 to 4635.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4635

```text
SecurityDetails <SctyDtls> contains the following FinancialInstrument55 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4635
   Name <Nm> [0..1] Text 4636
   ShortName <ShrtNm> [0..1] Text 4636
   SupplementaryIdentification <SplmtryId> [0..1] Text 4636
   ClassType <ClssTp> [0..1] Text 4637
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4637
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4637
   ProductGroup <PdctGrp> [0..1] Text 4637
Constraints
• IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
66.1.24.10.5.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the security by an ISIN.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4635 May 2026
```

