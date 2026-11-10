---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.57 RateType1Code"]
file_pages: [639, 640, 641]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.57 RateType1Code

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 639 to 641.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 639

```text
CodeName Name Definition
ACTU ActualAmount Price expressed as a currency and
amount per unit or per share.
7.2.2.57  RateType1Code
Definition: Specifies whether the rate is fixed or variable or a forfeit.
Type: CodeSet
CodeName Name Definition
FIXE Fixed Rate is fixed.
FORF Forfeit No specific repurchase rate applies to
the transaction Repo, only a forfeit.
VARI Variable Rate is variable.
7.2.2.58  Registration1Code
Definition: Specifies whether registration should occur upon receipt.
Type: CodeSet
CodeName Name Definition
NREG StreetName Hold the securities in street name. If
there is a standing instruction in place to
register on receipt, then this standing
instruction is to be ignored.
YREG Registered Register on receipt. If there is a standing
instruction in place to hold the securities
in street name, then this standing
instruction is to be ignored.
7.2.2.59  RejectionReason78Code
Definition: Specifies the reason why the instruction/cancellation request has a rejected status.
Type: CodeSet
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 639 February 2025
```

## File page 640

```text
CodeName Name Definition
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 640 February 2025
```

## File page 641

```text
CodeName Name Definition
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
trade amount, etc., values that differ
from the buy-side's calculations. Buy-
side may reject the trade if they feel that
the difference in calculations is too high.
CPTY UnknownDealExposure Deal or exposure is unknown.
DISC DisagreeWithCallAmount Party does not agree with the call
amount.
DISE DisagreeWithExposureAmount Party does not agree with the exposure
amount.
RESU MissingResultingAmount Resulting amount must be filled in as
exchange rate is present.
XRAT MissingExchangeRate Resulting amount is not allowed without
an exchange rate.
ACRU UnexpectedAccruedInterest Accrued interest is not applicable for this
type of security.
GAMN GrossAmountLessThanNetAmount Gross amount is less than net amount.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 641 February 2025
```

