---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.43 HoldIndicator6", "82.1.19.43.2 Reason <Rsn>"]
file_pages: [3026]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.43.2 Reason <Rsn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3026 to 3026.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3026

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.19.43.2  Reason <Rsn>
Presence: [0..*]
Definition: Specifies the reason of the registration status.
Reason <Rsn> contains the following elements (see "RegistrationReason5" on page 3006 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  3006
{Or     Code <Cd> [1..1] CodeSet 3006
Or}     Proprietary <Prtry> [1..1] ± 3007
   AdditionalInformation <AddtlInf> [0..1] Text 3007
82.1.19.44  DeliveryReturn3Choice
Definition: Choice of format for the delivery return information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3026
Or}   Proprietary <Prtry> [1..1] ± 3027
82.1.19.44.1  Code <Cd>
Presence: [1..1]
Definition: Delivery return expressed as an ISO 20022 code.
Datatype: "DeliveryReturn1Code" on page 3235
CodeName Name Definition
UNRE UnrecognisedDelivery Original delivery is not recognized.
DQUA WrongQuantity Wrong quantity delivered in the original
instruction.
DMON WrongSettlementAmount Wrong settlement amount settled in the
original delivery.
PART PartialDelivery Only a portion of the original transaction
quantity was delivered by the Central
Securities Depository (CSD).
SAFE AccountMissing Account information is missing in the
original delivery.
DUEB DueBiillMissing Due bill information missing in the
original delivery.
PARD PartialReturn Portion of the original transaction
quantity was returned by the receiver.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3026 August 2026
```

