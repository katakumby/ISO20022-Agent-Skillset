---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.3 SettlementDetails232", "35.1.26.3.2 SettlementTransactionCondition <SttlmTxCond>"]
file_pages: [1797]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.3.2 SettlementTransactionCondition <SttlmTxCond>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1797 to 1797.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1797

```text
HoldIndicator <HldInd> contains the following elements (see "HoldIndicator6" on page 1592 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 1593
   Reason <Rsn> [0..*] ± 1593
35.1.26.3.2  SettlementTransactionCondition <SttlmTxCond>
Presence: [0..*]
Definition: Conditions under which the order/trade is to be settled.
SettlementTransactionCondition <SttlmTxCond> contains one of the following elements (see
"SettlementTransactionCondition41Choice" on page 1641 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1641
Or}   Proprietary <Prtry> [1..1] ± 1642
35.1.26.3.3  SettlingCapacity <SttlgCpcty>
Presence: [0..1]
Definition: Role of a party in the settlement of the transaction.
SettlingCapacity <SttlgCpcty> contains one of the following elements (see "SettlingCapacity7Choice"
on page 1631 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1631
Or}   Proprietary <Prtry> [1..1] ± 1632
35.1.26.3.4  StampDutyTaxBasis <StmpDtyTaxBsis>
Presence: [0..1]
Definition: Specifies the stamp duty type or exemption reason applicable to the settlement transaction.
StampDutyTaxBasis <StmpDtyTaxBsis> contains the following elements (see
"GenericIdentification30" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.26.3.5  SecuritiesRTGS <SctiesRTGS>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1797 March 2026
```

