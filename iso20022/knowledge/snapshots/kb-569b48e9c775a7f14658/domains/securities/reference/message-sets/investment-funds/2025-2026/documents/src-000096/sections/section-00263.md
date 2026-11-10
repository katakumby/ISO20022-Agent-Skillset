---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["16 reda.005.001.03 InvestmentFundReportRequestV03", "16.4 Message Building Blocks", "16.4.4 ReportRequest <RptReq>", "16.4.4.2 Parameters <Params>"]
file_pages: [369]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.005.001.03"]
---

# 16.4.4.2 Parameters <Params>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 369 to 369.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 369

```text
CodeName Name Definition
NOCR NoCriteria No criteria.
16.4.4.2  Parameters <Params>
Presence: [1..1]
Definition: Report parameters.
Parameters <Params> contains the following FundParameters5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentDetails <FinInstrmDtls> [0..*] ± 369
   FundManagementCompany <FndMgmtCpny> [0..*] ± 369
   DateFrom <DtFr> [0..1] Date 370
   CountryOfDomicile <CtryOfDmcl> [0..1] CodeSet C2 370
   RegisteredDistributionCountry <RegdDstrbtnCtry> [0..*] CodeSet C2 370
16.4.4.2.1  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [0..*]
Definition: Financial instrument for which the report is requested.
FinancialInstrumentDetails <FinInstrmDtls> contains the following elements (see
"FinancialInstrument71" on page 4512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± C3, C4,
C5, C6,
C7
4513
   ShortName <ShrtNm> [0..1] Text 4514
   Name <Nm> [0..1] Text 4514
   SupplementaryIdentification <SplmtryId> [0..1] Text 4514
   ClassType <ClssTp> [0..1] Text 4514
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4514
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4515
   ProductGroup <PdctGrp> [0..1] Text 4515
16.4.4.2.2  FundManagementCompany <FndMgmtCpny>
Presence: [0..*]
Definition: Fund management company for which the report is requested.
Approved by the Securities SEG on 27 January 2026 reda.005.001.03
InvestmentFundReportRequestV03
Investment Funds - Maintenance 2025 - 2026 369 May 2026
```

