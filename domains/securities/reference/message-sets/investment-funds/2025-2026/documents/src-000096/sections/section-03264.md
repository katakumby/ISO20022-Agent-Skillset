---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.4 FinancialInstrument87", "66.1.18.4.9 BlockedHoldingDetails <BlckdHldgDtls>", "66.1.18.4.9.3 HoldingCertificateNumber <HldgCertNb>"]
file_pages: [4500]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.4.9.3 HoldingCertificateNumber <HldgCertNb>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4500 to 4500.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4500

```text
Definition: When an account is blocked at the level of fund or security, partially, this is the number of
units blocked.
Datatype: "DecimalNumber" on page 5400
66.1.18.4.9.3  HoldingCertificateNumber <HldgCertNb>
Presence: [0..1]
Definition: When an account is blocked at the level of fund or security, this specifies the certificate
number of the blocked units.
Datatype: "Max35Text" on page 5403
66.1.18.4.10  Pledging <Pldgg>
Presence: [0..1]
Definition: Specifies whether the holdings in the account are eligible for pledging.
Datatype: "Eligible1Code" on page 5295
CodeName Name Definition
ELIG Eligible Item is eligible.
NELI NotEligible Item is not eligible.
66.1.18.4.11  Collateral <Coll>
Presence: [0..1]
Definition: Specifies whether the holdings in the account are used as collateral.
Datatype: "Collateral1Code" on page 5285
CodeName Name Definition
COLL Collateral Item is used as collateral.
NCOL NotCollateral Item is not used as collateral.
66.1.18.4.12  ThirdPartyRights <ThrdPtyRghts>
Presence: [0..1]
Definition: Details of third party rights.
ThirdPartyRights <ThrdPtyRghts> contains the following elements (see "ThirdPartyRights2" on
page 4596 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 4596
   DateTime <DtTm> [0..1] DateTime 4596
   Holder <Hldr> [0..1] ± 4596
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4597
   Amount <Amt> [0..1] Amount C1, C13 4597
   Description <Desc> [0..1] Text 4597
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4500 May 2026
```

