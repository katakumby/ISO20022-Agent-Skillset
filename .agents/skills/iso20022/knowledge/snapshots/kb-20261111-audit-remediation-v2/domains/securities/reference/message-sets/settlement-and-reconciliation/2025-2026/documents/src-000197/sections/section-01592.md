---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.106 RejectionReason76Code"]
file_pages: [2123, 2124, 2125, 2126]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.106 RejectionReason76Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2123 to 2126.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2123

```text
CodeName Name Definition
SETR SettlementTransactionRejection Unrecognised or invalid settlement
transaction type.
SDUT LackOfStampDuty Required stamp duty information is
missing.
INPS PlaceOfSafekeeping Unrecognised, invalid or missing place of
safekeeping.
OTHR Other Other. See Narrative.
ICUS ReceivingDeliveringParty2 Unrecognised or invalid client of
delivering or receiving party 1.
ICAG ReceivingDeliveringParty1 Unrecognised or invalid participant of
delivering or receiving depository.
DEPT ReceivingDeliveringDepository Unrecognised or invalid depository.
IEXE ReceivingDeliveringParty3 Unrecognised or invalid client of
delivering or receiving party 2.
INVB InvalidBalance Instruction aims at using an invalid
balance.
INVL InvalidLink Invalid or unrecognized link.
INVN InvalidLotNumber Invalid or unrecognized lot number.
VALR InvalidRule Account servicer validation rule rejection.
INVE InvalidInvestorParty Unrecognised or invalid investor party.
May be used by an executing party to
reject an instruction for an investor (or
portfolio) for which it is not authorised to
act.
PLIS PlaceOfListing Unrecognised or invalid place of listing.
Used when the security identified is not
listed on the market supplied.
35.2.2.106  RejectionReason76Code
Definition: Specifies the reason why the instruction/cancellation request has a rejected status.
Type: CodeSet
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2123 March 2026
```

## File page 2124

```text
CodeName Name Definition
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2124 March 2026
```

## File page 2125

```text
CodeName Name Definition
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2125 March 2026
```

## File page 2126

```text
CodeName Name Definition
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
DISC DisagreeWithCallAmount Party does not agree with the call
amount.
DISE DisagreeWithExposureAmount Party does not agree with the exposure
amount.
DORD RegistrationRequestDataAndOrderRejection Disagreement between the data on the
registration request and the order.
FEEE FeeCommissionRejection Unrecognised or invalid fee or
commission.
SETR SettlementTransactionRejection Unrecognised or invalid settlement
transaction type.
TERM ClosingDateTimeRejection Unrecognised or invalid closing date/
time.
VASU VariableRateSupportRejection Unrecognised or invalid variable rate
support (repurchase agreement).
INPS PlaceOfSafekeeping Unrecognised, invalid or missing place of
safekeeping.
SDUT LackOfStampDuty Required stamp duty information is
missing.
FORF ForfeitAmount Unrecognised or invalid forfeit amount.
ICUS ReceivingDeliveringParty2 Unrecognised or invalid client of
delivering or receiving party 1.
ICAG ReceivingDeliveringParty1 Unrecognised or invalid participant of
delivering or receiving depository.
DEPT ReceivingDeliveringDepository Unrecognised or invalid depository.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2126 March 2026
```

