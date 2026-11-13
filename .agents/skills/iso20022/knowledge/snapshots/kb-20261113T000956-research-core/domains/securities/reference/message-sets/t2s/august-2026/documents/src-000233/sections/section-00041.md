---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["6 camt.065.001.01 LimitUtilisationJournalReportV01", "6.3 Constraints"]
file_pages: [75]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
topic_continuations: [{"constraint_ids": ["C5", "C6"], "until_heading": "6.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 76, "topic": "6.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00042.md"}]
---

# 6.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 75 to 75.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 6.3 Constraints topic continues in [Constraints continuation C5–C6 (file p76)](section-00042.md#file-page-76). Read the text before **6.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 75

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Amount <Amt> [1..1] ± 89
             MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 89
             TransactionIdentification <TxId> [0..1] Text 89
             AccountServicerReference <AcctSvcrRef> [0..1] Text 89
             ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 90
             AdditionalEntryInformation <AddtlNtryInf> [0..1] Text 90
Or}         BusinessError <BizErr> [1..*]  90
           Error <Err> [1..1]  90
{Or             Code <Cd> [1..1] CodeSet 90
Or}             Proprietary <Prtry> [1..1] Text 90
           Description <Desc> [0..1] Text 91
Or}     OperationalError <OprlErr> [1..*]  91
       Error <Err> [1..1]  91
{Or         Code <Cd> [1..1] CodeSet 91
Or}         Proprietary <Prtry> [1..1] Text 91
       Description <Desc> [0..1] Text 91
   SupplementaryData <SplmtryData> [0..*] ± C6 92
6.3 Constraints
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
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 75 August 2026
```

