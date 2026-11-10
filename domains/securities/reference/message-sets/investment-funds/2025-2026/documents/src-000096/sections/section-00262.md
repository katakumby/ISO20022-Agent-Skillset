---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["16 reda.005.001.03 InvestmentFundReportRequestV03", "16.4 Message Building Blocks", "16.4.4 ReportRequest <RptReq>"]
file_pages: [368]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.005.001.03"]
---

# 16.4.4 ReportRequest <RptReq>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 368 to 368.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 368

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
16.4.4 ReportRequest <RptReq>
Presence: [1..*]
Definition: Parameters for which the report is requested.
Impacted by: C8 "ReportParameterRule1"
ReportRequest <RptReq> contains one of the following FundParameters4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoCriteria <NoCrit> [1..1] CodeSet 368
Or}   Parameters <Params> [1..1]  369
     FinancialInstrumentDetails <FinInstrmDtls> [0..*] ± 369
     FundManagementCompany <FndMgmtCpny> [0..*] ± 369
     DateFrom <DtFr> [0..1] Date 370
     CountryOfDomicile <CtryOfDmcl> [0..1] CodeSet C2 370
     RegisteredDistributionCountry <RegdDstrbtnCtry> [0..*] CodeSet C2 370
Constraints
• ReportParameterRule1
If Parameters is present, at least one element in the list (Parameters/FundManagementCompany,
Parameters/FinancialInstrumentDetails, Parameters/DateFrom) must be present. More than one
element in the list (Parameters/FundManagementCompany, Parameters/FinancialInstrumentDetails,
Parameters/DateFrom) may be present.
On Condition
    /Parameters is present
Following Must be True
    /Parameters/FinancialInstrumentDetails[*] Must be present
 Or    /Parameters/FundManagementCompany[*] Must be present
 Or    /Parameters/DateFrom Must be present
16.4.4.1  NoCriteria <NoCrit>
Presence: [1..1]
Definition: Specifies that there is no criteria for the report. The request is a request for all reports, rather
than reports attributed to a specific fund manager, date or financial instrument.
Datatype: "NoCriteria1Code" on page 5331
Approved by the Securities SEG on 27 January 2026 reda.005.001.03
InvestmentFundReportRequestV03
Investment Funds - Maintenance 2025 - 2026 368 May 2026
```

