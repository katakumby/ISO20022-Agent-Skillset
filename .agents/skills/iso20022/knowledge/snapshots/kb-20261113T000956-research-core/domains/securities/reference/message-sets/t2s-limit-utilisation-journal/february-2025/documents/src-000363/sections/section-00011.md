---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["3 camt.065.001.01 LimitUtilisationJournalReportV01", "3.3 Constraints"]
file_pages: [11]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
topic_continuations: [{"constraint_ids": ["C5", "C6"], "until_heading": "3.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 12, "topic": "3.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/documents/src-000363/sections/section-00012.md"}]
---

# 3.3 Constraints

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 11 to 11.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 3.3 Constraints topic continues in [Constraints continuation C5–C6 (file p12)](section-00012.md#file-page-12). Read the text before **3.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 11

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             Amount <Amt> [1..1] ± 25
             MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 25
             TransactionIdentification <TxId> [0..1] Text 25
             AccountServicerReference <AcctSvcrRef> [0..1] Text 25
             ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 26
             AdditionalEntryInformation <AddtlNtryInf> [0..1] Text 26
Or}         BusinessError <BizErr> [1..*]  26
           Error <Err> [1..1]  26
{Or             Code <Cd> [1..1] CodeSet 26
Or}             Proprietary <Prtry> [1..1] Text 26
           Description <Desc> [0..1] Text 27
Or}     OperationalError <OprlErr> [1..*]  27
       Error <Err> [1..1]  27
{Or         Code <Cd> [1..1] CodeSet 27
Or}         Proprietary <Prtry> [1..1] Text 27
       Description <Desc> [0..1] Text 27
   SupplementaryData <SplmtryData> [0..*] ± C6 28
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
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 11 February 2025
```

