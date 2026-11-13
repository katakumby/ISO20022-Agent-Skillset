---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.43 PendingFailingSettlement1Code"]
file_pages: [865, 866]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.43 PendingFailingSettlement1Code

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 865 to 866.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 865

```text
CodeName Name Definition
origin and destination countries may be
the same country.
OND OvernightDeposit Transaction is linked to an overnight
deposit.
MGL MarginalLending Transaction is linked to the marginal
lending facility.
37.2.2.43  PendingFailingSettlement1Code
Definition: Specifies the reason the transaction/instruction is pending failing settlement, and the
settlement at the instruction settlement date is no longer possible.
Type: CodeSet
CodeName Name Definition
AWMO AwaitingMoney Securities have been delivered, but the
money is still expected from the
counterparty.
AWSH AwaitingSecuritiesFromCounterparty Securities have not yet been received
from the counterparty. If the settlement
instruction was a received against
payment, the cash has been delivered.
LAAW AwaitingOtherTransaction Awaiting settlement of a linked 'buy'.
DOCY AwaitingDocumentsOrEndorsementsFromYou Awaiting documents or endorsements
from you.
CLAT CounterpartyTooLateForSettlement Counterparty's instruction was too late
for settlement, (that is, received too late,
matching, or settlement problems were
solved too late).
CERT WrongCertificateNumbers Certificate number error.
MINO MinimumSettlementAmount Securities quantity is lower than the
minimum existing settlement quantity for
the instructed financial instrument.
PHSE PhysicalDeliveryDelay Settlement is physical, and there is a
delay in the delivery of the securities.
SBLO SecuritiesBlocked Securities are blocked, for example,
because of a corporate action event or
re-alignment.
DKNY CounterpartyReturnedSecurities Counterparty has returned, refused, or
does not recognize the securities.
STCD ConfirmationDiscrepancy Discrepancy in the settlement
confirmation.
BENO BeneficialOwnershipDisagreement Disagreement over beneficial ownership.
LACK LackOfSecurities Insufficient deliverable securities in your
account.
LATE TooLateForSettlement Settlement instruction was too late for
settlement, that is, received too late,
matching, or settlement problems were
solved too late.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 865 February 2025
```

## File page 866

```text
CodeName Name Definition
CANR CancellationConfirmationRequest Transaction suspended. Because the
suspension period is finished, the
cancellation or confirmation of
instructions is required.
MLAT MoneyTooLateForSettlement Payment for a buy of securities was
received after the cut-off time for
completing the settlement on a same
day basis.
OBJT UnderObjection Securities are stolen, in dispute, and
under objection.
DOCC AwaitingDocumentsOrEndorsementsFromCoun
terparty
Awaiting documents or endorsements
from the counterparty.
BLOC AccountBlocked Account is blocked, so no instruction can
settle.
CHAS EnquirySent Enquiry/chaser sent to the agent or
depository.
NEWI NewIssues Securities are new issues, and not yet
available/tradeable.
CLAC CounterpartyInsufficientSecurities Insufficient deliverable securities in the
counterparty's account, or counterparty
does not hold the securities.
PART TradeSettlesInPartials Trade will settle in partials.
CMON CounterpartyInsufficientMoney Insufficient money in counterparty's
account.
COLL SecuritiesPledgedAsCollateral Securities are not deliverable as they are
pledged as collateral.
DEPO RefusedDepositForIssueOfDepositaryReceipts Deposit of shares for the issuance of a
depositary receipt has been refused. The
allotment for depositary receipts granted
by the issuer would be exceeded by the
transaction.
FLIM MaximumForeignLimitReached Insufficient deliverable securities in your
account, as maximum foreign limit has
been reached.
NOFX NoForeignExchangeInstruction A foreign exchange instruction from you
is missing.
INCA IncomeAdjustementRequired Securities require income adjustment,
that is, dividend or interest.
LINK PendingLinkedInstruction Linked instruction is pending/failing.
BYIY BuyInProcedure A buy-in procedure has started on the
market, on your behalf, if your instruction
is a receipt, or on behalf of the
counterparty if the instruction is a
delivery.
CAIS AwaitingSecurities Awaiting securities from a corporate
action issue or other procedure(s), for
example, conversion, dematerialisation,
exchange, registration, stamping, and
splitting.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 866 February 2025
```

