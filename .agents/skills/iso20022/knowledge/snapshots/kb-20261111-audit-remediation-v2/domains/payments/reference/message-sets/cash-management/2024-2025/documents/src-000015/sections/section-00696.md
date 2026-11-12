---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.59 SystemStatus2Code"]
file_pages: [881, 882]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.59 SystemStatus2Code

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 881 to 882.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 881

```text
CodeName Name Definition
IBKC InterbankCutOff Event is the cutoff for interbank
payments.
SYSC SystemCutOff Event is the cutoff for the system.
SSSC NetSSSReservationCutOff Event is the cutoff for the securities
settlement system cash reservation
window.
REOP ResumeOperation Event is the expected resume time for a
TARGET component.
PCOT ProcessingCutOffTime Event is the cutoff time for the
processing of payments.
NPCT NewPaymentCutOffTime Event is the cutoff time for the receipt of
new commercial payments.
ESTF EndOfStandingFacilities Event is the cut off for the standing
facilities.
37.2.2.59  SystemStatus2Code
Definition: Specifies the status of a system.
Type: CodeSet
CodeName Name Definition
SUSP Suspended System is suspended, that is, not
operational.
ACTV Active System is functioning normally, that is,
operational.
CLSD Closed System is closed (eg. normal closure of
an RTGS).
CLSG Closing System needs to wait for completion of
intermediate internal activities before
going to a status Closed.
37.2.2.60  UnmatchedStatusReason1Code
Definition: Specifies the reason the transaction/instruction is unmatched.
Type: CodeSet
CodeName Name Definition
CMIS MatchingInstructionNotFound Matching instruction from the
counterparty could not be found.
DDAT DisagreementSettlementDate Counterparty disagrees with the
settlement date/time.
DELN DisagreementDirectionOfTrade Counterparty expects a delivery not a
receipt, or counterparty expects a receipt
not a delivery.
DEPT DisagreementPlaceOfSettlement Counterparty disagrees with the place of
settlement.
DMON DisagreementSettlementAmount Counterparty disagrees with the
settlement amount.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 881 February 2025
```

## File page 882

```text
CodeName Name Definition
DDEA DisagreementDealPrice Counterparty disagrees with the deal
price.
DQUA DisagreementQuantity Counterparty disagrees with the quantity
of the financial instrument.
CADE DisagreementRepurchaseCallDelay Repurchase call delay does not match.
SETR DisagreementSettlementTransaction Settlement transaction type does not
match.
DSEC DisagreementSecurity Counterparty disagrees with the security/
issue, for example, ISIN or a financial
instrument attribute differs.
VASU DisagreementVariableRateSupport Variable rate support does not match.
DTRA NotRecognised Counterparty does not recognise the
transaction.
RSPR DisagreementRepurchaseSpreadRate Repurchase spread rate does not match.
REPO DisagreementRepurchaseRate Repurchase rate does not match.
CLAT CounterpartyTooLateForMatching Counterparty's instruction was too late.
RERT DisagreementRepurchaseRateType Repurchase rate type does not match.
REPA DisagreementRepurchaseAmount Repurchase amount does not match.
REPP DisagreementRepurchasePremiumAmount Repurchase premium amount does not
match.
PHYS DisagreementPhysicalSettlement Counterparty's instructions is for physical
settlement, and yours is not, or vice
versa.
IIND DisagreementCommonReference Counterparty disagrees with the
common reference.
FRAP DisagreementPaymentCode Counterparty's instructions is for free
settlement, and yours is for settlement
against payment, or vice versa.
PLCE DisagreementPlaceOfTrade Place of trade does not match.
PODU PossibleDuplicateInstruction Instruction is a possible duplicate.
FORF DisagreementForfeitRepurchaseamount Repurchase forfeit amount does not
match.
REGD DisagreementRegistrationDetails Discrepancies exist in the registration
details linked to the transaction.
RTGS DisagreementRTGSSystem Counterparty indicates a settlement via
RTGS system and you indicate non-
RTGS settlement, or vice versa.
ICAG IncorrectAgent Counterparty indicated an incorrect
delivery or receiving agent.
CPCA CounterpartyCancelledInstruction Counterparty has cancelled the
transaction/instruction.
CHAR DisagreementChargesAmount Counterparty disagrees on the amount of
charges.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 882 February 2025
```

