---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.41 RejectionReason45Choice"]
file_pages: [1941, 1942, 1943]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.41 RejectionReason45Choice

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1941 to 1943.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1941

```text
35.1.29.41  RejectionReason45Choice
Definition: Choice of format for the rejection reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1941
Or}   Proprietary <Prtry> [1..1] ± 1944
35.1.29.41.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RejectionReason76Code" on page 2123
CodeName Name Definition
ULNK InvalidReference Linked reference is unknown.
SAFE SafekeepingAccountRejection Unrecognised or invalid message
sender's safekeeping account.
DQUA QuantityRejection Unrecognised or invalid instructed
quantity.
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
RTGS ImpossibleToUseTheRTGSSystemInstructed Not possible to use the RTGS system
instructed (NRTG or YRTG).
NCRR SettlementAmountCurrencyRejection Unrecognised or invalid settlement
amount currency.
DSEC InvalidSecurity Unrecognised or invalid financial
instrument identification.
DADR AddressDetailsRejection Address details are incorrect or cannot
be recognised.
INIR InstructionIrrevocable Instruction is irrevocable.
CANC OptionCancelled Option is not valid; it has been cancelled
by the market or service provider, and
cannot be responded to. Any responses
already processed against this option
are considered void and new responses
will be required.
INTV OptionInactive Option is not active and can no longer be
responded to. Any responses already
processed against this option will remain
valid, for example, expired option.
INVA InvalidForTaxAuthorities For tax reclaim, the reclaim is invalid for
the tax authorities.
REFT RefusedByTaxAuthorities Reclaim is refused by the tax authorities.
PHYS PhysicalSettlementImpossible Physical settlement is impossible for the
instructed financial instrument.
REFE ReferenceRejection Instruction has a reference identical to
another previously received instruction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1941 March 2026
```

## File page 1942

```text
CodeName Name Definition
LACK LackofSecurities Instructed position exceeds the eligible
balance.
LATE MarketDeadlineMissed Received after market deadline.
NMTY Mismatch Mismatch between option number and
option type.
OPNM OptionNumberRejection Unrecognised option number.
DMON SettlementAmountRejection Unrecognised or invalid settlement
amount.
OPTY InvalidOptionType Invalid option type.
DCAN RejectedSinceAlreadyCancelled Cancellation request was rejected since
the instruction has already been
cancelled.
DPRG RejectedSinceInProgress Cancellation request has been rejected
because the instruction process is in
progress or has been processed.
EVNM UnrecognisedIdentification Unrecognised event number.
STAT MissingStatutes Missing statutes or commercial register
or other legal documents.
STAM NotStampedOrSigned Financial instrument has not been
stamped and/or duly signed.
SIGN InvalidSignature Registration request does not have a
valid signature of the owner of the
financial instrument.
SHAR ShareholderNumberRejection Unrecognised, missing or invalid
shareholder number.
MINO MinimumSettlementQuantity Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
NRGM NoMatch More than one instruction match the
criteria.
MLEG MissingLegalPower Missing legal power for transfer.
BATC ProcessingBatchRejection Unrecognised or invalid processing
batch, that is, daytime/real-time while
only possible to settle in overnight batch.
CADE TransactionCallDelay Unrecognised or invalid transaction call
delay.
CASH CashAccount Unrecognised or invalid cash account.
DDEA DealPrice Unrecognised or invalid deal price.
OWNT TypeOfOwnershipRejection Type of ownership indicated is not
correct.
NRGN NotFoundRejection Instruction could not be found.
MUNO MultipleSettlementQuantity Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
REQW WrongRegistrationRequest Registration request to be completed by
the buyer and to be forwarded to the
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1942 March 2026
```

## File page 1943

```text
CodeName Name Definition
issuer is wrong. You have used the
registration request of a different issuer/
registrar.
TXST TaxStatusRejection Unrecognised or invalid tax status of the
securities instructed.
REPA TerminationTransactionAmount Unrecognised or invalid termination
transaction amount.
REPO RepurchaseRate Unrecognised or invalid repurchase rate.
REPP PremiumAmount Unrecognised or invalid premium
amount.
RREA DisagreementInRegistrationReason Registration reason indicated is not
correct.
REQM MissingRegistrationRequest Registration request to be completed by
the buyer and to be forwarded to the
issuer is missing.
RERT RepurchaseRateType Unrecognised or invalid repurchase rate
type.
RSPR SpreadRate Unrecognised or invalid spread rate.
SETS SettlementSystemMethodRejection Unrecognised or invalid settlement
system/method instructed.
DTRD TradeDate Unrecognised or invalid trade date or
requested trade date or future trade
date.
IIND CommonReferenceRejection Unrecognised, invalid or missing
common reference.
PLCE PlaceOfTrade Unrecognised or invalid place of trade.
INNA NarrativeInformationRejection Unrecognised or invalid service level
agreement pre-agreed narrative
information.
ICOL InsufficientCollateral Insufficient collateral proposed.
BPAR BusinessPartnerNumberRejection Unrecognised or invalid business partner
number.
BREF BankReferenceNumberRejection Unrecognised or invalid bank reference
number.
BUSE TypeOfOrderRejection Unrecognised or invalid type of order.
CAEV CorporateActionRejection Corporate action pending on the
financial instrument instructed.
CASY ImpossibleCashSettlementSystem Impossible standing arrangements
override instruction for the cash
settlement system.
COMC CommercializationContractRejection Unrecognised or invalid
commercialisation contract.
CONL ConcentrationLimitExceeded Concentration limit was exceeded.
CPTY UnknownDealExposure Deal or exposure is unknown.
DDAT SettlementDateRejection Unrecognised or invalid settlement date.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1943 March 2026
```

