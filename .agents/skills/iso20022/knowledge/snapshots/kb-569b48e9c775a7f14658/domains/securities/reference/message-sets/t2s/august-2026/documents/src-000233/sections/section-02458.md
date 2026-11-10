---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.108 PenaltyStatusReason2Code"]
file_pages: [3269, 3270]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.108 PenaltyStatusReason2Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3269 to 3270.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3269

```text
CodeName Name Definition
REMO Removed Removal of a cash penalty where
settlement cannot be performed for
reasons that are independent from any
of the CSD participants or the CSD.
82.2.2.108  PenaltyStatusReason2Code
Definition: Specifies the reason for the status of the penalty.
Type: CodeSet
CodeName Name Definition
UPDT Updated Penalty has been updated.
SUSP TradingSuspended Penalty was removed becuase of ISIN
suspension from trading.
TECH TechnicalImpossibilities Penalty was removed becuase there
were thecnical imposssibilities at the
CSD level that prevent settlement, such
as: a failure of the infrastructure
components, a cyber-attack, network
problems.
SWIC Switched Penalty has been switched between the
failing and non-failing party.
SESU SettlementSuspended Penalty was removed becuase of ISIN
suspension from settlement due to a
reconciliation issue under Article 65 (2)
and (6) of the RTS on CSD
Requirements.
SEMP SettlementOnMultiplePlatforms Settlement on multiple platforms where
one of the platforms is closed for
settlement (either cash or securities).
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
82.2.2.109  PenaltyType1Code
Definition: Specifies the type of penalty.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3269 August 2026
```

## File page 3270

```text
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
82.2.2.110  PendingProcessingReason5Code
Definition: Specifies the reason the transaction/instruction is pending or failing settlement. Settlement
on the instructed settlement date is still possible, status is pending. Settlement on the instructed
settlement date is no longer possible, status is failing.
Type: CodeSet
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3270 August 2026
```

