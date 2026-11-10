---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["10 camt.011.001.08 ModifyLimitV08", "10.4 Message Building Blocks", "10.4.2 LimitDetails <LmtDtls>", "10.4.2.1 LimitIdentification <LmtId>", "10.4.2.1.1 Current <Cur>"]
file_pages: [429]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.011.001.08"]
---

# 10.4.2.1.1 Current <Cur>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 429 to 429.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 429

```text
10.4.2.1.1  Current <Cur>
Presence: [1..1]
Definition: Identification of the current limit.
Impacted by: C3 "BilateralLimitCounterparty1Rule", C4 "BilateralLimitCounterparty2Rule"
Current <Cur> contains the following LimitIdentification8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [0..1] ± 429
   BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[0..1] ± 430
   Type <Tp> [1..1]  430
{Or     Code <Cd> [1..1] CodeSet 430
Or}     Proprietary <Prtry> [1..1] Text 432
   AccountOwner <AcctOwnr> [0..1] ± 432
   AccountIdentification <AcctId> [0..1] ± 433
Constraints
• BilateralLimitCounterparty1Rule
If Type is MULT, then BilateralLimitCounterpartyIdentification is not allowed.
On Condition
    /Type/Code is equal to value 'Multilateral'
Following Must be True
    /BilateralLimitCounterpartyIdentification Must be absent
• BilateralLimitCounterparty2Rule
If Type is BILI or NELI or INBI, then BilateralLimitCounterpartyIdentification must be present.
On Condition
    /Type/Code is equal to value 'Bilateral'
 Or    /Type/Code is equal to value 'NetBilateral'
 Or    /Type/Code is equal to value 'IndirectBilateral'
Following Must be True
    /BilateralLimitCounterpartyIdentification Must be present
10.4.2.1.1.1  SystemIdentification <SysId>
Presence: [0..1]
Definition: Identification of a particular cash clearing system.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 429 February 2025
```

