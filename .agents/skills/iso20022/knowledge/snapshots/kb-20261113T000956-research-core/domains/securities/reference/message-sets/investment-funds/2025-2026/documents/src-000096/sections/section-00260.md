---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["16 reda.005.001.03 InvestmentFundReportRequestV03", "16.2 Structure"]
file_pages: [366]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.005.001.03"]
---

# 16.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 366 to 366.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 366

```text
16.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <InvstmtFndRptReq> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 367
   PreviousReference <PrvsRef> [0..1] ± 367
   RelatedReference <RltdRef> [0..1] ± 367
   ReportRequest <RptReq> [1..*]  C8 368
{Or     NoCriteria <NoCrit> [1..1] CodeSet 368
Or}     Parameters <Params> [1..1]  369
       FinancialInstrumentDetails <FinInstrmDtls> [0..*] ± 369
       FundManagementCompany <FndMgmtCpny> [0..*] ± 369
       DateFrom <DtFr> [0..1] Date 370
       CountryOfDomicile <CtryOfDmcl> [0..1] CodeSet C2 370
       RegisteredDistributionCountry <RegdDstrbtnCtry> [0..*] CodeSet C2 370
16.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C4 DescriptionUsageRule
Description must be used alone as the last resort.
C5 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C6 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
Approved by the Securities SEG on 27 January 2026 reda.005.001.03
InvestmentFundReportRequestV03
Investment Funds - Maintenance 2025 - 2026 366 May 2026
```

