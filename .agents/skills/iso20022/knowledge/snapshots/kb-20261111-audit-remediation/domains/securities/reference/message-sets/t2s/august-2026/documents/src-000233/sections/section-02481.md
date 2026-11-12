---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.156 SettlementType1Code"]
file_pages: [3303]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.156 SettlementType1Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3303 to 3303.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3303

```text
CodeName Name Definition
PART PartialAllowed Partial settlement is allowed.
NPAR PartialNotAllowed Partial settlement is not allowed.
PARC PartialSettlementCashThresholdAllowed Partial settlement is allowed but must
satisfy a cash value minimum (value
defined in static data).
PARQ PartialSettlementQuantityThresholdAllowed Partial settlement is allowed but must
satisfy a minimum quantity of securities
(quantity defined in static data).
82.2.2.156  SettlementType1Code
Definition: Indicates how an option trade is settled.
Type: CodeSet
CodeName Name Definition
PRIN Principal Option trade is settled as principal.
NETO NettedOff Option trade is netted off against another
trade.
82.2.2.157  SettlementUnitType1Code
Definition: Type of settlement foreseen for the security.
Type: CodeSet
CodeName Name Definition
FAMT FaceAmount Represent the face amount, for example
the principal of a debt instrument.
UNIT Unit Represent the unit as a number, for
example a number of shares.
82.2.2.158  SettleStyle1Code
Definition: Specifies when the option contract settles.
Type: CodeSet
CodeName Name Definition
SETC SettleOnClose Settlement is only allowed on the closing
of the future contract.
SETO SettleOnOpen Settlement is only allowed on the
opening of the future contract.
82.2.2.159  SettlingCapacity2Code
Definition: Specifies the role of the party in the settlement of the transaction.
Type: CodeSet
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3303 August 2026
```

