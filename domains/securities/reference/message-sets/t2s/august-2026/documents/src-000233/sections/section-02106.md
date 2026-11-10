---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.11 SecuritiesBalanceType6Choice", "82.1.5.11.2 Proprietary <Prtry>"]
file_pages: [2860]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.11.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2860 to 2860.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2860

```text
CodeName Name Definition
UNRG Unregistered Balance of securities that could not be
registered due to foreign ownership
limitation.
ISSU Issued In issuer agent / depository
communication, balance of issued
financial instruments for which legal
documentation has been received.
QUAS QuasiIssued In issuer agent / depository
communication, balance of issued
financial instruments for which legal
documentation has not yet been
received.
LODE PendingOnLoanDelivery Balance of financial instruments that are
pending delivery in relation to a lending
transaction.
82.1.5.11.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Sub-balance expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.5.12  Balance9
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account. A securities balance is calculated from the sum of securities' receipts minus the sum
of securities' deliveries.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 2860
   Quantity <Qty> [1..1] ± 2861
82.1.5.12.1  ShortLongIndicator <ShrtLngInd>
Presence: [0..1]
Definition: Indication that the position is short or long.
Datatype: "ShortLong1Code" on page 3304
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2860 August 2026
```

