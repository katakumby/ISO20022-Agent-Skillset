---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.16 AdditionalPhysicalOrRegistrationDetails <AddtlPhysOrRegnDtls>", "26.4.18.3 MatchingStatus <MtchgSts>"]
file_pages: [876, 877, 878]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.18.3 MatchingStatus <MtchgSts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 876 to 878.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 876

```text
InferredMatchingStatus <IfrrdMtchgSts> contains one of the following elements (see
"MatchingStatus24Choice" on page 1963 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C1 1964
Or   Unmatched <Umtchd> [1..1]  1964
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1965
Or}     Reason <Rsn> [1..*]  1965
       Code <Cd> [1..1]  1965
{Or         Code <Cd> [1..1] CodeSet 1966
Or}         Proprietary <Prtry> [1..1] ± 1968
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1968
Or}   Proprietary <Prtry> [1..1] ± 1968
26.4.18.3  MatchingStatus <MtchgSts>
Presence: [0..1]
Definition: Provides the matching status of the instruction.
MatchingStatus <MtchgSts> contains one of the following elements (see "MatchingStatus24Choice"
on page 1963 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Matched <Mtchd> [1..1] ± C1 1964
Or   Unmatched <Umtchd> [1..1]  1964
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1965
Or}     Reason <Rsn> [1..*]  1965
       Code <Cd> [1..1]  1965
{Or         Code <Cd> [1..1] CodeSet 1966
Or}         Proprietary <Prtry> [1..1] ± 1968
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1968
Or}   Proprietary <Prtry> [1..1] ± 1968
26.4.18.4  SettlementStatus <SttlmSts>
Presence: [0..1]
Definition: Provides the status of settlement of a transaction.
Impacted by: C46 "PendingToFailingRule"
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 876 March 2026
```

## File page 877

```text
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus32Choice" on page 1860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1]  1861
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1862
Or}     Reason <Rsn> [1..*]  1862
       Code <Cd> [1..1]  1862
{Or         Code <Cd> [1..1] CodeSet 1862
Or}         Proprietary <Prtry> [1..1] ± 1865
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1866
Or   Failing <Flng> [1..1]  1866
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1866
Or}     Reason <Rsn> [1..*]  1866
       Code <Cd> [1..1]  1867
{Or         Code <Cd> [1..1] CodeSet 1867
Or}         Proprietary <Prtry> [1..1] ± 1870
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1871
Or}   Proprietary <Prtry> [1..1] ± 1871
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
26.4.19 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C69 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 877 March 2026
```

## File page 878

```text
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 878 March 2026
```

