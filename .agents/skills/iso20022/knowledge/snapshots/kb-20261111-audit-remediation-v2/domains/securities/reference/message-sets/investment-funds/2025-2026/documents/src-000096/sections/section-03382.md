---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.9 InvestmentAccount73", "66.1.24.9.19 RoundingDetails <RndgDtls>"]
file_pages: [4626]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.9.19 RoundingDetails <RndgDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4626 to 4626.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4626

```text
FinancialInstrumentDetails <FinInstrmDtls> contains the following elements (see
"FinancialInstrument87" on page 4496 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4496
   Name <Nm> [0..1] Text 4497
   ShortName <ShrtNm> [0..1] Text 4497
   SupplementaryIdentification <SplmtryId> [0..1] Text 4497
   ClassType <ClssTp> [0..1] Text 4498
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4498
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4498
   ProductGroup <PdctGrp> [0..1] Text 4498
   BlockedHoldingDetails <BlckdHldgDtls> [0..1]  C18,
C26,
C27,
C28
4498
     BlockedHolding <BlckdHldg> [1..1] CodeSet 4499
     PartialHoldingUnits <PrtlHldgUnits> [0..1] Quantity 4499
     HoldingCertificateNumber <HldgCertNb> [0..1] Text 4500
   Pledging <Pldgg> [0..1] CodeSet 4500
   Collateral <Coll> [0..1] CodeSet 4500
   ThirdPartyRights <ThrdPtyRghts> [0..1] ± 4500
   FundOwnership <FndOwnrsh> [0..1] CodeSet 4501
   FundIntention <FndIntntn> [0..1] CodeSet 4501
   OperationalStatus <OprlSts> [0..1] CodeSet 4501
Constraints
• IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
66.1.24.9.19  RoundingDetails <RndgDtls>
Presence: [0..1]
Definition: Parameters to be applied on deal amount for orders when the amount is a fractional number.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4626 May 2026
```

