---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.6 RejectionReason52Choice", "7.1.28.6.1 Code <Cd>"]
file_pages: [590, 591]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.6.1 Code <Cd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 590 to 591.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 590

```text
7.1.28.6.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RejectionReason78Code" on page 639
CodeName Name Definition
ASTM AgreementStartDate Agreement start date is missing or
invalid.
BUSE TypeOfOrderRejection Unrecognised or invalid type of order.
CADE TransactionCallDelay Unrecognised or invalid transaction call
delay.
COMC CommercializationContractRejection Unrecognised or invalid
commercialisation contract.
DDAT SettlementDateRejection Unrecognised or invalid settlement date.
DDEA DealPrice Unrecognised or invalid deal price.
DMON SettlementAmountRejection Unrecognised or invalid settlement
amount.
DQUA QuantityRejection Unrecognised or invalid instructed
quantity.
DSEC InvalidSecurity Unrecognised or invalid financial
instrument identification.
DTRD TradeDate Unrecognised or invalid trade date or
requested trade date or future trade
date.
FEEE FeeCommissionRejection Unrecognised or invalid fee or
commission.
FORF ForfeitAmount Unrecognised or invalid forfeit amount.
IEXE ReceivingDeliveringParty3 Unrecognised or invalid client of
delivering or receiving party 2.
IIND CommonReferenceRejection Unrecognised, invalid or missing
common reference.
INNA NarrativeInformationRejection Unrecognised or invalid service level
agreement pre-agreed narrative
information.
NARR NarrativeReason See narrative field for reason.
NCRR SettlementAmountCurrencyRejection Unrecognised or invalid settlement
amount currency.
ODNP OrderDateNotProvided Order entry date is missing.
PLCE PlaceOfTrade Unrecognised or invalid place of trade.
QUNP QuantityUnitType Quantity unit type is not provided.
REFE ReferenceRejection Instruction has a reference identical to
another previously received instruction.
CTRA ClosingTransactionAmount Unrecognised or invalid closing closing
amount.
REPO RepurchaseRate Unrecognised or invalid repurchase rate.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 590 February 2025
```

## File page 591

```text
CodeName Name Definition
REPP PremiumAmount Unrecognised or invalid premium
amount.
RERT RepurchaseRateType Unrecognised or invalid repurchase rate
type.
RSPR SpreadRate Unrecognised or invalid spread rate.
SAFE SafekeepingAccountRejection Unrecognised or invalid message
sender's safekeeping account.
SETR SettlementTransactionRejection Unrecognised or invalid settlement
transaction type.
SETS SettlementSystemMethodRejection Unrecognised or invalid settlement
system/method instructed.
TERM ClosingDateTimeRejection Unrecognised or invalid closing date/
time.
TNAR TransactionNoticeAlreadyAcceptedOrRejected A message with the same Transaction
Notice Reference, Market Member, and
Intermediary has already been
processed.
TNIU TransactionNoticeIDUnknown The combination of the Transaction
Notice Reference, Market Member, and
Intermediary is unknown.
TQHI TradedQuantityHigherThanOriginalOrderQuantit
y
Market member executed the order
exceeding the requested quantity.
TQNP TradedSecuritiesQuantity Traded securities quantity not provided.
TXST TaxStatusRejection Unrecognised or invalid tax status of the
securities instructed.
ULNK InvalidReference Linked reference is unknown.
VASU VariableRateSupportRejection Unrecognised or invalid variable rate
support (repurchase agreement).
INIR InstructionIrrevocable Instruction is irrevocable.
OPNM OptionNumberRejection Unrecognised option number.
OPTY InvalidOptionType Invalid option type.
UKWN UnknownSymbol Financial instrument's symbol has not
been recognized.
EXLI ExceedsLimit Countervalue of the order exceeds the
allowed trading limit or quote exceeds
limit.
INPR InvalidPrice Price does not comply with the financial
instrument's characteristics.
PRIC PriceExceeds Price in the execution exceeds the order
price.
EQTY QuantityExceeds Quantity in the execution exceeds the
ordered quantity.
SIDE WrongSide Order is for the wrong side.
CADI CalculationDifference Primarily used when the Notice of
Execution received by the buy-side
contains fees, gross trade amount, net
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 591 February 2025
```

