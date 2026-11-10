---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.180 UnmatchedReason11Code"]
file_pages: [3317, 3318]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.180 UnmatchedReason11Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3317 to 3318.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3317

```text
CodeName Name Definition
SQYA SquareYard Measure of a surface, one yard by one
yard.
USBA USBarrel Unit of volume equal to 158, 9873 litre.
USFO USFluidOunce Unit of volume equal to 2, 957353
centilitre.
USGA USGallon Unit of volume that is equal to 8 pints.
USPI USPint Unit of volume that is equal to 473 cubic
centimetres.
USQA USQuart Unit of volume that is equal to 2 pints.
USTN USTon Measure of weight, in the US 2000 lb
(short ton).
YARD Yard Unit of length equal to 3 feet or 0.9144
metre.
GBOU GBOunce Unit of weight equal to a sixteenth of a
pound.
ACRE Acre Unit of measure equal to 4, 840 square
yards.
ARES Are Unit of measure equal to a 100 square
meters.
HECT Hectare Unit of measure that is equal to 10, 000
square meters.
82.2.2.180  UnmatchedReason11Code
Definition: Specifies the reason the transaction, transfer or settlement instruction is unmatched.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
ACRU AccruedInterestAmount1 Accrued interest amount does not
match.
IIND CommonReference Common reference does not match.
CPCA CounterpartyCancelled Counterparty cancelled their instruction.
CLAT CounterpartyTooLateForMatching Counterparty's instruction was too late
for matching.
NCRR CurrencySettlementAmount Settlement amount currency does not
match.
DDEA DealPrice Deal price does not match.
DMCT AutomaticGeneration Disagreement on automatic generation
of market claim or transformation.
DCMX CumEx Disagreement if trade was executed cum
or ex.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3317 August 2026
```

## File page 3318

```text
CodeName Name Definition
DSEC FinancialInstrument Financial instrument identification does
not match, for example, ISIN, financial
instrument attributes differs.
DQUA FinancialInstrumentQuantity Quantity of financial instruments does
not match.
INVE InvestorParty Investor party does not match.
LEOG LetterOfGuarantee Counterparty is for settlement through
letter of guarantee, your instruction is
not, or vice versa.
LATE MarketDeadlineMissed Your instruction was too late for
matching.
MIME MissingMarketSide Missing market execution details.
CMIS NoMatch A matching instruction from your
counterparty could not be found.
NMAS NoMatchingStarted Matching process has not yet started.
DTRA NotRecognised Counterparty has been contacted or
contacted us, and does not recognise
the transaction.
OTHR Other Proprietary unmatched reason code
described in a narrative field.
FRAP PaymentCode Payment type does not match: your
instruction is free of payment, your
counterparty's instruction is against
payment or vice versa.
PHYS PhysicalSettlement Counterparty's instruction is physical
settlement, your instruction is not, or vice
versa.
PLIS PlaceOfListing Place of listing does not match.
INPS PlaceOfSafekeeping Place of safekeeping information does
not allow matching to take place.
PLCE PlaceOfTrade Place of trade does not match.
PODU PossibleDuplicate Instruction has not been matched. It is a
possible duplicate instruction.
DEPT ReceivingDeliveringDepository Depository does not match.
ICAG ReceivingDeliveringParty1 Participant of delivering or receiving
depository does not match.
ICUS ReceivingDeliveringParty2 Client of delivering or receiving party 1
does not match.
IEXE ReceivingDeliveringParty3 Client of delivering or receiving party 2
does not match.
REGD RegistrationDetails Registration details linked to the
transaction are incorrect.
RTGS RTGSSystem Counterparty is for Real Time Gross
Settlement (RTGS) system, you are for
non-RTGS or vice versa.
SAFE SafekeepingAccount Safekeeping account used as matching
criteria on the market concerned does
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3318 August 2026
```

