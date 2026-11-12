---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.20 LetterOfGuarantee4Choice", "82.1.19.20.1 Indicator <Ind>"]
file_pages: [3000, 3001]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.20.1 Indicator <Ind>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3000 to 3001.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3000

```text
82.1.19.20.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether physical settlement may be executed using a letter of guarantee or if the
physical certificates should be used.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.19.20.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Letter of guarantee information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.21  SettlementTransactionCondition34Choice
Definition: Choice of format for the settlement transaction conditions.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3000
Or}   Proprietary <Prtry> [1..1] ± 3002
82.1.19.21.1  Code <Cd>
Presence: [1..1]
Definition: Settlement conditions expressed as an ISO 20022 code.
Datatype: "SettlementTransactionCondition12Code" on page 3301
CodeName Name Definition
ADEA AcceptAfterRegularSettlementDeadline Settlement is on a bilaterally accepted
transaction that is to be accepted
beyond the regular settlement deadline.
ASGN Assignement Transfer of ownership of the asset to
another party during the closing of an
option.
BUTC BuytoCover Transaction is a buy to cover.
CLEN Clean Tax-exempt financial instruments are to
be settled.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3000 August 2026
```

## File page 3001

```text
CodeName Name Definition
DLWM DeliveryWithoutMatching Matching receipt instruction not required
(only for concerned international or
national central securities depositories).
DIRT Dirty Taxable financial instruments are to be
settled.
DRAW Drawn Settlement transactions relates to drawn
securities.
EXER Exercised Settlement transaction relates to options,
futures or derivatives that are exercised.
EXPI Expired Settlement transaction relates to options,
futures or derivatives that have expired.
FRCL FreeCleanSettlement Delivery will be made free of payment
but a clean payment order will be sent.
KNOC KnockedOut Settlement transaction relates to options,
futures or derivatives that are expired
worthless.
NOMC NoAutomaticMarketClaim No market claim should be automatically
generated.
NACT NotAccountingRelated Security transaction is not for
accounting.
PENS PendingSale Position to cover the pending sale will be
available by contractual settlement date
(accounting information).
PHYS Physical Securities are to be physically settled.
RHYP Rehypothecation Collateral position is available for other
purposes (for example, onwards
delivery).
RPTO Reporting Relates to a transaction that is for
reporting purposes only.
RESI Residual Relates to transaction on a security that
is not eligible at the Central Security
Depository (CSD) but for which the
payment will be enacted by the central
securities depository.
SHOR ShortSell Account is used for short sale orders.
SPDL SpecialDelivery Settlement transactions to be settled
with special delivery.
SPST SplitSettlement Money and financial instruments settle in
different locations.
TRAN Transformation Transaction resulting from a
transformation.
TRIP TripartySegregation Securities are not be delivered but
segregated following triparty collateral
transaction.
UNEX Unexposed Delivery cannot be performed until
money is received.
INTS InternalisedSettlement The instruction was settled by the
settlement internaliser/account servicer
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3001 August 2026
```

