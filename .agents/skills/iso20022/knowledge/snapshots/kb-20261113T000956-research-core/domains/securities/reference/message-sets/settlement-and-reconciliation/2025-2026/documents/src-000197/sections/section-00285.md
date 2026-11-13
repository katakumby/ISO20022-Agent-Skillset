---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "12.4 Message Building Blocks", "12.4.6 AdditionalQueryParameters <AddtlQryParams>", "12.4.6.2 Reason <Rsn>", "12.4.6.2.7 PendingReason <PdgRsn>", "12.4.6.2.7.2 Proprietary <Prtry>"]
file_pages: [427]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.021.001.09"]
---

# 12.4.6.2.7.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 427 to 427.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 427

```text
CodeName Name Definition
SETS SettlementSystemMethodModified Settlement system/method has been
modified at central securities depository
to allow settlement.
IAAD StatusReasonInvestigation Pending reason being investigated.
PRSY SystemOnHold Transaction was put on hold/frozen by
the system.
TAMM TradeAmendedInMarket Trade is being amended in the market.
PART TradeSettlesInPartials Trade will settle in partials.
DENO UnavailableDeliverableDenominatedQuantity Quantity instructed does not match the
denomination available/deliverable.
Physical securities need to be obtained
in deliverable denominated quantities.
VLDA ValidForTaxAuthorities For tax reclaim, the event is pending, the
tax reclaim is valid for the tax authorities.
PREA YourInstructionOnHold Your instruction is a preadvice, that is,
for matching only.
12.4.6.2.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
12.4.6.2.8  FailingReason <FlngRsn>
Presence: [0..1]
Definition: Specifies the reason why the instruction has a failing settlement status.
FailingReason <FlngRsn> contains one of the following elements (see "FailingReason9Choice" on
page 1960 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1960
Or}   Proprietary <Prtry> [1..1] ± 1963
12.4.6.2.9  PendingProcessingReason <PdgPrcgRsn>
Presence: [0..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 427 March 2026
```

