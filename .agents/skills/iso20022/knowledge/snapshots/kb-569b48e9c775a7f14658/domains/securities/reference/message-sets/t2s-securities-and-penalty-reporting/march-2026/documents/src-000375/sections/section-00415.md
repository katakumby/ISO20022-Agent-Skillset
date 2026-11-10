---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.46 PenaltyType1Code"]
file_pages: [519, 520]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.46 PenaltyType1Code

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 519 to 520.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 519

```text
CodeName Name Definition
RALO Reallocated Re-allocation of a late matching fail
penalty from the instructing party to the
delivering/receiving party.
OTHR Other See narrative.
NEWP NewPenalty Penalty is new.
INTS InternalisedSettlement Penalty is not computed because the
settlement has been internalised.
INSO Insolvency Penalty was removed becuase
insolvency proceedings are opened
against the failing participant.
CORP CorporateAction Specifies that due to a specific corporate
action, the security does no longer
exists.
NOSU NotSubject Penalty is not computed or removed
because the security is not subject to
penalties.
7.2.2.46  PenaltyType1Code
Definition: Specifies the type of penalty.
Type: CodeSet
CodeName Name Definition
LMFP LateMatchingFailedPenalty Applies from the intended settlement
date until the matching date.
The penalty is charged to the participant
who was last to enter or modify the
relevant settlement instruction (for
example, "accepted timestamp" is later
than the one of the counterparty's
instruction) for the periods between the
intended settlement date and the day of
matching of the instruction.
SEFP SettlementFailedPenalty Penalties apply to instructions that fail to
settle on the intended settlement date. A
settlement instruction that "fails to settle
on that business day" must be
understood as a settlement instruction
that is not cancelled and remaining to be
settled, fully or partially, by the time of
the end of processing of the relevant cut-
off.
7.2.2.47  PendingProcessingReason5Code
Definition: Specifies the reason the transaction/instruction is pending or failing settlement. Settlement
on the instructed settlement date is still possible, status is pending. Settlement on the instructed
settlement date is no longer possible, status is failing.
Type: CodeSet
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 519 March 2026
```

## File page 520

```text
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
CAIS AwaitingSecurities Awaiting financial instruments from a
corporate action or other procedure, for
example, conversion, dematerialisation,
exchange, registration, stamping,
splitting.
DOCY AwaitingDocumentsOrEndorsementsFromYou Awaiting documents or endorsements
from you.
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
MUNO MultipleSettlementAmount Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
GLOB GlobalFormSecurities Settlement cannot be executed; financial
instruments are in global form.
PREA YourInstructionOnHold Your instruction is a preadvice, that is,
for matching only.
YCOL CollateralShortage Insufficient collateral in your account to
execute the instruction.
COLL SecuritiesPledgedAsCollateral Financial instruments are not deliverable
as they are pledged as collateral.
FLIM MaximumForeignLimitReached Insufficient deliverable financial
instruments in your account as maximum
foreign limit has been reached.
NOFX NoForeignExchangeInstruction A foreign exchange instruction from you
is missing.
LACK LackOfSecurities Insufficient financial instruments in your
account.
LALO SecuritiesLoanedOut Financial instruments are out on loan.
MONY InsufficientMoney Insufficient money in your account.
MINO MinimumSettlementAmount Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
OTHR Other Other. See Narrative.
DENO UnavailableDeliverableDenominatedQuantity Quantity instructed does not match the
denomination available/deliverable.
Physical securities need to be obtained
in deliverable denominated quantities.
LIQU InsufficientCentralBankLiquidity Central bank liquidity is insufficient.
CERT WrongCertificatesNumbers Certificate number error.
NEXT NextProcess Next process is launched. No processing
pending problems to be reported.
PRSY SystemOnHold Transaction was put on hold/frozen by
the system.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 520 March 2026
```

