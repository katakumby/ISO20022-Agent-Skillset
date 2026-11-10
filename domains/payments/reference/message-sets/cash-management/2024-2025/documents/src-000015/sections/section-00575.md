---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["33 camt.101.001.02 CreateLimitV02", "33.4 Message Building Blocks", "33.4.2 LimitData <LmtData>", "33.4.2.1 LimitIdentification <LmtId>"]
file_pages: [748]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.101.001.02"]
---

# 33.4.2.1 LimitIdentification <LmtId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 748 to 748.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 748

```text
LimitData <LmtData> contains the following LimitStructure6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LimitIdentification <LmtId> [1..1]  C3, C4 748
     SystemIdentification <SysId> [0..1] ± 749
     BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 749
     Type <Tp> [1..1]  750
{Or       Code <Cd> [1..1] CodeSet 750
Or}       Proprietary <Prtry> [1..1] Text 752
     AccountOwner <AcctOwnr> [0..1] ± 752
     AccountIdentification <AcctId> [0..1] ± 752
   StartDateTime <StartDtTm> [0..1] ± 753
   Amount <Amt> [1..1] ± 753
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 753
33.4.2.1  LimitIdentification <LmtId>
Presence: [1..1]
Definition: Identification of the default limit.
Impacted by: C3 "BilateralLimitCounterparty1Rule", C4 "BilateralLimitCounterparty2Rule"
LimitIdentification <LmtId> contains the following LimitIdentification8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [0..1] ± 749
   BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 749
   Type <Tp> [1..1]  750
{Or     Code <Cd> [1..1] CodeSet 750
Or}     Proprietary <Prtry> [1..1] Text 752
   AccountOwner <AcctOwnr> [0..1] ± 752
   AccountIdentification <AcctId> [0..1] ± 752
Constraints
• BilateralLimitCounterparty1Rule
If Type is MULT, then BilateralLimitCounterpartyIdentification is not allowed.
On Condition
    /Type/Code is equal to value 'Multilateral'
Approved by the Payments SEG on 04 February 2025 camt.101.001.02 CreateLimitV02
Cash Management - Maintenance 2024 - 2025 748 February 2025
```

