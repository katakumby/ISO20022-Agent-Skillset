---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.3 Constraints"]
file_pages: [19]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.3 Constraints

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 19 to 19.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 19

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or           Code <Cd> [1..1] CodeSet 108
Or}           Proprietary <Prtry> [1..1] Text 108
       Service <Svc> [0..1]  108
         SystemIdentification <SysId> [1..1] ± 108
         SystemCurrency <SysCcy> [0..1] CodeSet C1 109
       InvoiceDate <InvcDt> [1..1] Date 109
       BillingIdentification <BllgId> [1..1] Text 109
       BillingPeriod <BllgPrd> [1..1] ± 109
       CancellationReason <CxlRsn> [1..1]  109
{Or         Code <Cd> [1..1] Text 110
Or}         Proprietary <Prtry> [1..1] Text 110
Or}     OperationalError <OprlErr> [1..*]  110
       Error <Err> [1..1]  110
{Or         Code <Cd> [1..1] CodeSet 110
Or}         Proprietary <Prtry> [1..1] Text 111
       Description <Desc> [0..1] Text 111
   SupplementaryData <SplmtryData> [0..*] ± C6 111
3.3 Constraints
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
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 19 December 2025
```

