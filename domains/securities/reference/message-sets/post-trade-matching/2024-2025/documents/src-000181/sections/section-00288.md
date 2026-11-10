---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.43 Order23", "7.1.19.43.27 NumberOfDaysAccrued <NbOfDaysAcrd>"]
file_pages: [348]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.43.27 NumberOfDaysAccrued <NbOfDaysAcrd>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 348 to 348.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 348

```text
Commission <Comssn> contains the following elements (see "Commission25" on page 250 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 250
   Commission <Comssn> [1..1] ± 251
   RecipientIdentification <RcptId> [0..1]  251
     BIC <BIC> [1..1] IdentifierSet C3 251
     ProprietaryIdentification <PrtryId> [1..1] ± 252
     NameAndAddress <NmAndAdr> [0..1]  252
       Name <Nm> [1..1] Text 252
       Address <Adr> [0..1]  253
         AddressType <AdrTp> [0..1] CodeSet 253
         AddressLine <AdrLine> [0..5] Text 253
         StreetName <StrtNm> [0..1] Text 253
         BuildingNumber <BldgNb> [0..1] Text 254
         PostCode <PstCd> [0..1] Text 254
         TownName <TwnNm> [0..1] Text 254
         CountrySubDivision <CtrySubDvsn> [0..1] Text 254
         Country <Ctry> [1..1] CodeSet C4 254
   CalculationDate <ClctnDt> [0..1] Date 254
   TotalCommission <TtlComssn> [0..1] ± 254
   TotalVATAmount <TtlVATAmt> [0..1] Amount C1, C9 255
   VATRate <VATRate> [0..1] Rate 255
7.1.19.43.27  NumberOfDaysAccrued <NbOfDaysAcrd>
Presence: [0..1]
Definition: Number of days on which the interest rate accrues (daily accrual note).
Impacted by: C25 "NumberRule"
Datatype: "Max3Number" on page 666
Constraints
• NumberRule
If Number is negative, then Sign must be present.
7.1.19.43.28  GiveUpNumberOfDays <GvUpNbOfDays>
Presence: [0..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 348 February 2025
```

