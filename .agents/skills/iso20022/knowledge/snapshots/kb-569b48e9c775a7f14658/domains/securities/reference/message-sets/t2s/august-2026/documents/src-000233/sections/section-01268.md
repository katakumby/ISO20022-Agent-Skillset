---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.3 Constraints"]
file_pages: [1801]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1801 to 1801.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1801

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             InvestorCSD <InvstrCSD> [0..1]  2032
{Or               OrganisationIdentification <OrgId> [1..1] ± 2032
Or}               CombinedIdentification <CmbndId> [1..1] ± 2032
             TechnicalIssuerCSD <TechIssrCSD> [0..1]  2032
{Or               OrganisationIdentification <OrgId> [1..1] ± 2033
Or}               CombinedIdentification <CmbndId> [1..1] ± 2033
             IssuanceAccount <IssncAcct> [0..*]  2033
               IssuanceAccount <IssncAcct> [1..1] ± 2033
               PrimaryAccountIndicator <PmryAcctInd> [1..1] Indicator 2034
Or}       BusinessError <BizErr> [1..*]  2034
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C6, C7,
C8, C9,
C12
2034
         BusinessError <BizErr> [1..*]  2035
           Error <Err> [1..1]  2036
{Or             Code <Cd> [1..1] CodeSet 2036
Or}             Proprietary <Prtry> [1..1] Text 2036
           Description <Desc> [0..1] Text 2036
Or}     OperationalError <OprlErr> [1..*]  2036
       Error <Err> [1..1]  2037
{Or         Code <Cd> [1..1] CodeSet 2037
Or}         Proprietary <Prtry> [1..1] Text 2037
       Description <Desc> [0..1] Text 2037
   SupplementaryData <SplmtryData> [0..*] ± C14 2037
32.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1801 August 2026
```

