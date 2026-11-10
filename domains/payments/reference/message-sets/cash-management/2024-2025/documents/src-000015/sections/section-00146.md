---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.1 PaymentCommonInformation <PmtCmonInf>", "5.4.2.1.1.3 CommonStatus <CmonSts>", "5.4.2.1.1.3.3 Reason <Rsn>"]
file_pages: [240, 241]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.1.3.3 Reason <Rsn>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 240 to 241.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 240

```text
DateTime <DtTm> contains one of the following elements (see "DateAndDateTime2Choice" on
page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
5.4.2.1.1.3.3  Reason <Rsn>
Presence: [0..*]
Definition: Reason provided for the status of a transfer.
Reason <Rsn> contains one of the following PaymentStatusReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unmatched <Umtchd> [1..1] CodeSet 240
Or   Cancelled <Canc> [1..1] CodeSet 242
Or   Suspended <Sspd> [1..1] CodeSet 242
Or   PendingFailingSettlement <PdgFlngSttlm> [1..1] CodeSet 242
Or   PendingSettlement <PdgSttlm> [1..1] CodeSet 245
Or   ProprietaryRejection <PrtryRjctn> [1..1]  247
     ProprietaryStatusReason <PrtryStsRsn> [1..1] Text 247
     Reason <Rsn> [1..1] Text 247
Or}   Proprietary <Prtry> [1..1] Text 248
5.4.2.1.1.3.3.1  Unmatched <Umtchd>
Presence: [1..1]
Definition: Reason why the payment status is unmatched.
Datatype: "UnmatchedStatusReason1Code" on page 881
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
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 240 February 2025
```

## File page 241

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
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 241 February 2025
```

