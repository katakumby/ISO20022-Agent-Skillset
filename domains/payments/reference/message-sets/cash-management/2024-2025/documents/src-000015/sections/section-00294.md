---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["10 camt.011.001.08 ModifyLimitV08", "10.4 Message Building Blocks"]
file_pages: [425, 426]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.011.001.08"]
---

# 10.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 425 to 426.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 425

```text
C6 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C7 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C8 OldLimitOrLimitAmendmentPresenceRule
OldLimitValueSet or LimitValueAmendment must be absent, both can be absent.
C9 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
10.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
10.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 811 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 812
   CreationDateTime <CreDtTm> [0..1] DateTime 812
10.4.2 LimitDetails <LmtDtls>
Presence: [0..*]
Definition: Identifies one particular limit set by the member and managed by the transaction
administrator.
Impacted by: C8 "OldLimitOrLimitAmendmentPresenceRule"
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 425 February 2025
```

## File page 426

```text
LimitDetails <LmtDtls> contains the following LimitStructure5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LimitIdentification <LmtId> [1..1]  427
{Or     Current <Cur> [1..1]  C3, C4 429
       SystemIdentification <SysId> [0..1] ± 429
       BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 430
       Type <Tp> [1..1]  430
{Or         Code <Cd> [1..1] CodeSet 430
Or}         Proprietary <Prtry> [1..1] Text 432
       AccountOwner <AcctOwnr> [0..1] ± 432
       AccountIdentification <AcctId> [0..1] ± 433
Or     Default <Dflt> [1..1]  C3, C4 433
       SystemIdentification <SysId> [0..1] ± 434
       BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 434
       Type <Tp> [1..1]  435
{Or         Code <Cd> [1..1] CodeSet 435
Or}         Proprietary <Prtry> [1..1] Text 437
       AccountOwner <AcctOwnr> [0..1] ± 437
       AccountIdentification <AcctId> [0..1] ± 438
Or     AllCurrent <AllCur> [1..1]  438
       SystemIdentification <SysId> [0..1] ± 439
       Type <Tp> [1..1]  439
{Or         Code <Cd> [1..1] CodeSet 439
Or}         Proprietary <Prtry> [1..1] Text 441
       AccountOwner <AcctOwnr> [0..1] ± 441
       AccountIdentification <AcctId> [0..1] ± 442
Or}     AllDefault <AllDflt> [1..1]  442
       SystemIdentification <SysId> [0..1] ± 443
       Type <Tp> [1..1]  443
{Or         Code <Cd> [1..1] CodeSet 443
Or}         Proprietary <Prtry> [1..1] Text 445
       AccountOwner <AcctOwnr> [0..1] ± 445
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 426 February 2025
```

