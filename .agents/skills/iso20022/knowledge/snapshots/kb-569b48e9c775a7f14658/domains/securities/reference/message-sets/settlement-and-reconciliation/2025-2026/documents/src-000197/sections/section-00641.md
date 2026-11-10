---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.4 Message Building Blocks", "28.4.2 ProcessingStatus <PrcgSts>", "28.4.2.3 PendingProcessing <PdgPrcg>", "28.4.2.3.2 Reason <Rsn>", "28.4.2.3.2.1 Code <Cd>", "28.4.2.3.2.1.2 Proprietary <Prtry>"]
file_pages: [966]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.4.2.3.2.1.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 966 to 966.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 966

```text
CodeName Name Definition
LACK LackOfSecurities Insufficient financial instruments in your
account.
FLIM MaximumForeignLimitReached Insufficient deliverable financial
instruments in your account as maximum
foreign limit has been reached.
MINO MinimumSettlementAmount Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
MUNO MultipleSettlementAmount Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
NEXT NextProcess Next process is launched. No processing
pending problems to be reported.
NOFX NoForeignExchangeInstruction A foreign exchange instruction from you
is missing.
OTHR Other Other. See Narrative.
LALO SecuritiesLoanedOut Financial instruments are out on loan.
COLL SecuritiesPledgedAsCollateral Financial instruments are not deliverable
as they are pledged as collateral.
DENO UnavailableDeliverableDenominatedQuantity Quantity instructed does not match the
denomination available/deliverable.
Physical securities need to be obtained
in deliverable denominated quantities.
CERT WrongCertificatesNumbers Certificate number error.
28.4.2.3.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
28.4.2.3.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
28.4.2.4  Rejected <Rjctd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 966 March 2026
```

