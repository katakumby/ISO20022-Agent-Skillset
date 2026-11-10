---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.3 Constraints"]
file_pages: [248]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.3 Constraints

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 248 to 248.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 248

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or           Code <Cd> [1..1] CodeSet 337
Or}           Proprietary <Prtry> [1..1] Text 337
       Service <Svc> [0..1]  337
         SystemIdentification <SysId> [1..1] ± 337
         SystemCurrency <SysCcy> [0..1] CodeSet C1 338
       InvoiceDate <InvcDt> [1..1] Date 338
       BillingIdentification <BllgId> [1..1] Text 338
       BillingPeriod <BllgPrd> [1..1] ± 338
       CancellationReason <CxlRsn> [1..1]  338
{Or         Code <Cd> [1..1] Text 339
Or}         Proprietary <Prtry> [1..1] Text 339
Or}     OperationalError <OprlErr> [1..*]  339
       Error <Err> [1..1]  339
{Or         Code <Cd> [1..1] CodeSet 339
Or}         Proprietary <Prtry> [1..1] Text 340
       Description <Desc> [0..1] Text 340
   SupplementaryData <SplmtryData> [0..*] ± C6 340
15.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 248 August 2026
```

