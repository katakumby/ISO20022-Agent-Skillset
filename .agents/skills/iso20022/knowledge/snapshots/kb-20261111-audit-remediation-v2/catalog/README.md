# ISO 20022 retrieval guide

Start here, select a reference, then follow its detailed type, table or diagram links. Consult the supplied original when the reference records uncertainty or a visual check is needed. Draft extraction is searchable evidence, not a reviewed interpretation.

## Find a reference

- [Messages by exact identifier and family](messages.md), with [machine-readable metadata](messages.json).
- [Message-set and publication indexes](message-sets.md), with [metadata](message-sets.json).
- [Shared participants](participants.md) and [business flows](flows.md).
- [Concepts and schema declarations](concepts.md) and [diagrams](diagrams.md).
- [Source identities and all loose/archive occurrences](sources.json).
- [Native embedded-object dispositions](../shared/reference/native-assets/index.md), distinguishing verified bitmap legends from unresolved native Visio semantics.
- [Corpus processing and validation report](../tracking/completion-report.md), including explicit remaining review limits.
- [Coverage summary](coverage-summary.json), [issues](../tracking/issues.md), [validation](../tracking/validation.json), and [resume checkpoint](../tracking/checkpoint.json).

Family keys such as `sese.023` are navigation aids. Exact identifiers and namespaces determine canonical message identity. Do not combine different definitions, infer version equivalence, or classify a collection solely by message prefix.

## Repository map

| Area | Purpose |
| --- | --- |
| [raw-input](../evidence/omitted/a0200aa6832074f7851bd4f6.md) | Supplied message-set collections, unchanged original files and archive |
| [shared](../shared/index.md) | Headers, reusable administration, code publications and scoped participant records |
| [securities](../domains/securities/index.md) | Securities collections and individual T2S message sets |
| [payments](../domains/payments/index.md) | Initiation, clearing/settlement, operational cash management, bank-to-customer reporting |
| [templates](../evidence/omitted/af03ff89b349afdbf776d0d5.md) | Reference page conventions; templates are not converted knowledge |
| [tracking](../tracking/conversion-status.md) | Sources, jobs, issues, review evidence and durable checkpoints |
| [tools](../evidence/omitted/9cea6a1607559a2e7aefc9e3.md) | Focused local extraction, lookup, index and validation helpers |
| [work](../evidence/omitted/00e13ed7af55b27622f1d6ea.md) | Temporary extraction, exact cell/paragraph/page inventories and renderer working files |

## Collection routing

Raw folder names and supplied bytes are preserved. Membership follows the source collection; business-area codes are separate metadata.

| Supplied folder | Output area | Collection |
| --- | --- | --- |
| business_application_header | shared | Business Application Header |
| ExternalCodeSets | shared | External code sets |
| settlement_and_reconciliation | securities | Settlement and Reconciliation |
| corporate_actions | securities | Corporate Actions |
| securities_events_general_meeting_proxy_voting | securities | Meetings |
| collateral_management_collateral_management | securities | Collateral Management |
| central_counterparty_clearing_ccp_clearing | securities | CCP Clearing |
| post_trade_matching | securities | Post-Trade Matching |
| investment_funds | securities | Investment Funds |
| transactions_and_financial_instruments_data_reporting_fitrr | securities | Transactions and Financial Instruments Data Reporting |
| target2securities_t2s | securities | TARGET2-Securities |
| payments_initiation | payments | Payments Initiation |
| payments_clearing_and_settlement | payments | Payments Clearing and Settlement |
| cash_management | payments | Cash Management |
| banktocustomer_cash_management | payments | Bank-to-Customer Cash Management |

T2S contains14 individual archive message sets. Reusable T2S Administration and Business File Header definitions have shared canonical references; the remaining child collections stay under securities. Preserve each archive-member boundary and publication edition. The participant reference library is shared across output domains, with contextual roles kept distinct.

## Local lookup

The read-only catalog commands use Python and the existing metadata cache. Extraction dependencies are documented in [tools](../evidence/omitted/9cea6a1607559a2e7aefc9e3.md). Start PowerShell in the repository directory, then run:

```powershell
$kbRoot = (Get-Location).Path
python -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" list --kind message-index --limit 10
python -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" message sese.023 --limit 10
python -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" message head.002.001.01 --limit 1
python -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" roles sese.023.001.13 --limit 5
python -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" search "account servicer" --kind participant --limit 10
python -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" search "reversal" --kind business-flow --limit 10
```

Set `$kbRoot` to the repository directory when running from elsewhere. The default root is the parent of the invoked `tools/kb.py`, so `--root` can be omitted for that checkout. If Python is not on PATH, invoke your Python executable explicitly. The `-X utf8` flag keeps JSON output in UTF-8 across Windows console encodings.

After maintained metadata changes, rebuild the derived indexes and validate with the appropriate extraction dependencies available:

```powershell
python -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" rebuild
python -X utf8 "$kbRoot\tools\kb.py" --root "$kbRoot" validate --checksums
```

Results contain canonical paths, source identities, review status and limitations. The default is 10 results and the maximum is 100. A bounded search does not prove absence. Follow the relevant source's detailed locator before making a substantive claim.

## Interpretation boundaries

A functional role is contextual: the same institution may be an account owner in one relationship and an account servicer in another. Similar labels across publications do not establish equivalence. Participant records retain source scope and source-supported relationships.

BAH and Business File Header are distinct exact definitions. Operational cash management and bank-to-customer reporting retain separate collection memberships even where both contain `camt` messages. Schema-only collections expose missing business documentation. External code-type names do not constitute a current code-list enumeration.

All generated indexes derive from reference metadata and the source identity register. `search.sqlite` is a disposable search cache; it is not an independently maintained knowledge source. No skills are created or installed by these helpers.
